/*
 * Copyright (c) 2021, The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <android-base/properties.h>
#include <cstring>
#define _REALLY_INCLUDE_SYS__SYSTEM_PROPERTIES_H_
#include <sys/_system_properties.h>

#include "vendor_init.h"

namespace {
struct Variant {
    const char* region;
    const char* brand;
    const char* device;
    const char* model;
    const char* market_name;
    const char* fingerprint;
};

// Preserve the original match priority: CN, INDIA, then GLOBAL.
constexpr Variant kVariants[] = {
    {"CN", "Redmi", "peridot", "24069RA21C", "Redmi Turbo 3",
     "Redmi/peridot/peridot:16/BP2A.250605.031.A3/OS3.0.305.0.WNPCNXM:user/release-keys"},
    {"INDIA", "POCO", "peridot_in", "24069PC21I", "POCO F6",
     "POCO/peridot_in/peridot:16/BP2A.250605.031.A3/OS3.0.303.0.WNPINXM:user/release-keys"},
    {"GLOBAL", "POCO", "peridot_global", "24069PC21G", "POCO F6",
     "POCO/peridot_global/peridot:16/BP2A.250605.031.A3/OS3.0.6.0.WNPMIXM:user/release-keys"},
};

void property_override(const char* prop, const char* value) {
    auto* pi = const_cast<prop_info*>(__system_property_find(prop));
    if (pi)
        __system_property_update(pi, value, std::strlen(value));
    else
        __system_property_add(prop, std::strlen(prop), value, std::strlen(value));
}
}  // namespace

void vendor_load_properties(void) {
    const std::string region = android::base::GetProperty("ro.boot.hwc", "");
    for (const auto& variant : kVariants) {
        if (region.find(variant.region) == std::string::npos) continue;

        property_override("ro.build.fingerprint", variant.fingerprint);
        property_override("ro.product.brand", variant.brand);
        property_override("ro.product.device", variant.device);
        property_override("ro.product.model", variant.model);
        property_override("ro.product.marketname", variant.market_name);
        property_override("bluetooth.device.default_name", variant.market_name);
        property_override("ro.product.odm.name", variant.device);
        property_override("ro.product.odm.model", variant.model);
        property_override("vendor.usb.product_string", variant.market_name);
        return;
    }
}
