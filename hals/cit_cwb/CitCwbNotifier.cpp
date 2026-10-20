/*
 * Copyright (c) 2026 Project Mia
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <android/binder_auto_utils.h>
#include <android/binder_manager.h>
#include <android/binder_stability.h>
#include <android-base/logging.h>

#include <chrono>
#include <condition_variable>
#include <cstdint>
#include <mutex>
#include <string_view>
#include <thread>

namespace {
using Clock = std::chrono::steady_clock;
constexpr auto kInterval = std::chrono::milliseconds(200);
constexpr char kDescriptor[] = "vendor.xiaomi.sensor.citsensorservice.ICitSensorService";
constexpr char kService[] = "vendor.xiaomi.sensor.citsensorservice.ICitSensorService/default";

// Client-side class: prepareTransaction writes the descriptor's interface token.
// No local service is instantiated or registered.
void* onCreate(void* args) { return args; }
void onDestroy(void*) {}
binder_status_t onTransact(AIBinder*, transaction_code_t, const AParcel*, AParcel*) {
    return STATUS_UNKNOWN_TRANSACTION;
}

class Worker {
  public:
    Worker() { std::thread([this] { run(); }).detach(); }

    void notify(bool presented) {
        {
            std::lock_guard lock(mMutex);
            if (!presented) ++mGeneration;
            mActive = presented;
            mPending = presented;
        }
        mCondition.notify_one();
    }

  private:
    bool current(uint64_t generation) {
        std::lock_guard lock(mMutex);
        return mActive && mGeneration == generation;
    }

    void report(std::string_view stage, int32_t code) {
        if (stage.empty()) {
            if (!mSucceeded) {
                LOG(INFO) << "CIT CWB: first primary capture request accepted";
                mSucceeded = true;
            }
        } else if (stage != mLastStage || code != mLastCode) {
            LOG(WARNING) << "CIT CWB: " << stage << " failed: " << code;
        }
        mLastStage = stage;
        mLastCode = code;
    }

    void capture(uint64_t generation) {
        // Binding, liveness checks and cache ownership belong only to this worker.
        if (mBinder.get() && !AIBinder_isAlive(mBinder.get())) mBinder.set(nullptr);
        if (!mBinder.get()) {
            mBinder.set(AServiceManager_checkService(kService));
            if (!mBinder.get()) {
                report("checkService", STATUS_NAME_NOT_FOUND);
                return;
            }
            static const AIBinder_Class* const clazz =
                    AIBinder_Class_define(kDescriptor, onCreate, onDestroy, onTransact);
            if (!clazz || !AIBinder_associateClass(mBinder.get(), clazz)) {
                mBinder.set(nullptr);
                report("associateClass", STATUS_BAD_TYPE);
                return;
            }
        }
        if (!current(generation)) return;

        // Runtime-verified V1 NDK wire contract (transaction 9):
        // int triggerCwbDump(int displayId, int type, bool force).
        // Primary forced CWB produces real RGB callbacks used by CIT's ALS path.
        ndk::ScopedAParcel in, out;
        binder_status_t status = AIBinder_prepareTransaction(mBinder.get(), in.getR());
        if (status == STATUS_OK) status = AParcel_writeInt32(in.get(), 0);
        if (status == STATUS_OK) status = AParcel_writeInt32(in.get(), 0);
        if (status == STATUS_OK) status = AParcel_writeBool(in.get(), true);
        // OFF can cancel work during lookup/preparation. Once dispatched, CIT
        // rejects OFF itself; never hold the state lock across a Binder call.
        if (!current(generation)) return;
        if (status == STATUS_OK) {
            status = AIBinder_transact(mBinder.get(), 9, in.getR(), out.getR(),
                                       FLAG_PRIVATE_VENDOR);
        }
        ndk::ScopedAStatus reply;
        if (status == STATUS_OK) status = AParcel_readStatusHeader(out.get(), reply.getR());
        int32_t result = 0;
        if (status == STATUS_OK && AStatus_isOk(reply.get())) {
            status = AParcel_readInt32(out.get(), &result);
        }
        if (status != STATUS_OK) {
            // Includes DEAD_OBJECT. A later real frame can reconnect, without
            // a death callback racing the worker's binder ownership.
            mBinder.set(nullptr);
            report("transport", status);
        } else if (!AStatus_isOk(reply.get())) {
            report("service exception", AStatus_getExceptionCode(reply.get()));
        } else if (result != 0) {
            report("triggerCwbDump", result);
        } else {
            report({}, 0);
        }
    }

    void run() {
        std::unique_lock lock(mMutex);
        for (;;) {
            mCondition.wait(lock, [this] { return mActive && mPending; });
            // A deadline only throttles an existing event; it never creates one.
            if (Clock::now() < mNext) {
                mCondition.wait_until(lock, mNext, [this] { return !mActive; });
                continue;
            }
            const uint64_t generation = mGeneration;
            mPending = false;
            lock.unlock();
            capture(generation);
            lock.lock();
            // Measure from completion so slow lookup/IPC cannot bunch captures.
            mNext = Clock::now() + kInterval;
        }
    }

    std::mutex mMutex;
    std::condition_variable mCondition;
    bool mActive = false;
    bool mPending = false;
    uint64_t mGeneration = 0;
    Clock::time_point mNext{};
    ndk::SpAIBinder mBinder;
    std::string_view mLastStage;
    int32_t mLastCode = 0;
    bool mSucceeded = false;
};

Worker& worker() {
    // Intentionally retained for process lifetime. The HWC loader must retain
    // this DSO (RTLD_NODELETE), including its detached worker's executable code.
    static Worker* const instance = new Worker;
    return *instance;
}

__attribute__((constructor)) void initialize() {
    // HWC notifications perform no thread creation, service lookup or IPC.
    (void)worker();
}
}  // namespace

// true: real primary-ON frame committed; false: primary power left ON.
extern "C" __attribute__((visibility("default"))) void xiaomi_cit_cwb_notify(bool frame_presented) {
    worker().notify(frame_presented);
}
