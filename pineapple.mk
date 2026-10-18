
#
# Copyright (C) 2026 Project Mia
#
# SPDX-License-Identifier: Apache-2.0
#

# A/B
$(call inherit-product, $(SRC_TARGET_DIR)/product/virtual_ab_ota/launch_with_vendor_ramdisk.mk)

# APEX
$(call inherit-product, $(SRC_TARGET_DIR)/product/updatable_apex.mk)

# Dalvik vm configs
$(call inherit-product, frameworks/native/build/phone-xhdpi-6144-dalvik-heap.mk)

# Generic ramdisk allow list
$(call inherit-product, $(SRC_TARGET_DIR)/product/generic_ramdisk.mk)

# pKVM
$(call inherit-product, packages/modules/Virtualization/apex/product_packages.mk)

# Project ID Quota
$(call inherit-product, $(SRC_TARGET_DIR)/product/emulated_storage.mk)

# A/B OTA
ifeq ($(TARGET_BUILD_VARIANT),user)
POSTINSTALL_FS_TYPE := erofs
else
POSTINSTALL_FS_TYPE := ext4
endif

PRODUCT_PACKAGES += \
    android.hardware.boot-service.qti \
    android.hardware.boot-service.qti.recovery \
    checkpoint_gc \
    otapreopt_script \
    update_engine \
    update_engine_sideload \
    update_verifier

AB_OTA_POSTINSTALL_CONFIG += \
    RUN_POSTINSTALL_system=true \
    POSTINSTALL_PATH_system=system/bin/otapreopt_script \
    FILESYSTEM_TYPE_system=ext4 \
    POSTINSTALL_OPTIONAL_system=true

AB_OTA_POSTINSTALL_CONFIG += \
    RUN_POSTINSTALL_vendor=true \
    POSTINSTALL_PATH_vendor=bin/checkpoint_gc \
    FILESYSTEM_TYPE_vendor=ext4 \
    POSTINSTALL_OPTIONAL_vendor=true

# API
BOARD_SHIPPING_API_LEVEL := 34
PRODUCT_SHIPPING_API_LEVEL := $(BOARD_SHIPPING_API_LEVEL)

# Architecture
TARGET_BOARD_PLATFORM := pineapple

# Audio
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/audio/audio_effects.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_cliffs/audio_effects.xml \
    $(LOCAL_PATH)/configs/audio/audio_policy_configuration.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_cliffs/audio_policy_configuration.xml

# AVB
BOARD_AVB_ENABLE := true

# Camera
PRODUCT_PACKAGES += \
    libcamera2ndk_vendor

PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.hardware.camera.flash-autofocus.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.camera.flash-autofocus.xml \
    frameworks/native/data/etc/android.hardware.camera.front.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.camera.front.xml \
    frameworks/native/data/etc/android.hardware.camera.full.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.camera.full.xml \
    frameworks/native/data/etc/android.hardware.camera.raw.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.camera.raw.xml

# Contexthub
PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.hardware.context_hub.xml:$(TARGET_COPY_OUT_ODM)/etc/permissions/android.hardware.context_hub.xml

# Display
PRODUCT_PACKAGES += \
    android.hardware.graphics.mapper@4.0-impl-qti-display \
    libgpu_tonemapper \
    vendor.qti.hardware.display.allocator-service \
    vendor.qti.hardware.display.composer-service \
    vendor.qti.hardware.display.composer3-V3-ndk.vendor \
    vendor.qti.hardware.display.config-V11-ndk.vendor \
    vendor.qti.hardware.display.demura-service \
    vendor.qti.hardware.display.demura-V1-ndk.vendor

$(foreach display_id, 4630947195234848131 4630947033261136259 4630946545580055171, \
    $(eval PRODUCT_COPY_FILES += \
        $(LOCAL_PATH)/configs/display/displayconfig.xml:$(TARGET_COPY_OUT_VENDOR)/etc/displayconfig/display_id_$(display_id).xml \
    ))

# DRM
PRODUCT_PACKAGES += \
    android.hardware.drm-service.clearkey

# Fastbootd
PRODUCT_PACKAGES += \
    fastbootd

# GNSS
PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.hardware.location.gps.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.location.gps.xml

# Health
PRODUCT_PACKAGES += \
    android.hardware.health-service.qti \
    android.hardware.health-service.qti_recovery

# Init
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/init/fstab.qcom:$(TARGET_COPY_OUT_VENDOR_RAMDISK)/first_stage_ramdisk/fstab.qcom

PRODUCT_PACKAGES += \
    charger_fw_fstab.qti \
    fstab.qcom \
    init.peridot.rc \
    init.target.rc \
    ueventd-odm.rc

# IR
PRODUCT_PACKAGES += \
    android.hardware.ir-service.xiaomi

PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.hardware.consumerir.xml:$(TARGET_COPY_OUT_ODM)/etc/permissions/android.hardware.consumerir.xml

# Keymint
PRODUCT_PACKAGES += \
    android.hardware.authsecret-service.nxp \
    android.hardware.security.keymint3-service.strongbox.nxp \
    android.hardware.weaver-service.nxp

PRODUCT_PACKAGES += \
    android.hardware.hardware_keystore_V3.xml

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/hal_uuid_map.xml:$(TARGET_COPY_OUT_VENDOR)/etc/hal_uuid_map_peridot.xml

PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.software.device_id_attestation.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.software.device_id_attestation.xml \
    frameworks/native/data/etc/android.hardware.keystore.app_attest_key.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.hardware.keystore.app_attest_key.xml

# Media
PRODUCT_COPY_FILES += \
    vendor/qcom/opensource/audio-hal/primary-hal/configs/common/codec2/media_codecs_c2_audio.xml:$(TARGET_COPY_OUT_VENDOR)/etc/media_codecs_c2_audio.xml

PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/media/media_codecs_cliffs_v0.xml:$(TARGET_COPY_OUT_VENDOR)/etc/media_codecs_cliffs_v0.xml \
    $(LOCAL_PATH)/configs/media/media_codecs_performance_cliffs_v0.xml:$(TARGET_COPY_OUT_VENDOR)/etc/media_codecs_performance_cliffs_v0.xml \
    $(LOCAL_PATH)/configs/media/media_profiles_cliffs_v0.xml:$(TARGET_COPY_OUT_VENDOR)/etc/media_profiles_cliffs_v0.xml \
    $(LOCAL_PATH)/configs/media/video_system_specs.json:$(TARGET_COPY_OUT_VENDOR)/etc/media_cliffs_v0/video_system_specs.json \

# Mlipay
PRODUCT_PACKAGES += \
    IFAAService

# Namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Partitions
PRODUCT_USE_DYNAMIC_PARTITIONS := true

# Verified Boot
PRODUCT_COPY_FILES += \
    frameworks/native/data/etc/android.software.verified_boot.xml:$(TARGET_COPY_OUT_VENDOR)/etc/permissions/android.software.verified_boot.xml
