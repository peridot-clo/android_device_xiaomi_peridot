#
# Copyright (C) 2026 Project Mia
#
# SPDX-License-Identifier: Apache-2.0
#

# PATH
DEVICE_PATH := device/xiaomi/peridot
HARDWARE_PATH := hardware/xiaomi
AUDIO_HAL_DIR := vendor/qcom/opensource/audio-hal/primary-hal

# Architecture
TARGET_ARCH := arm64
TARGET_ARCH_VARIANT := armv8-2a-dotprod
TARGET_CPU_ABI := arm64-v8a
TARGET_CPU_ABI2 :=
TARGET_CPU_VARIANT := generic
TARGET_CPU_VARIANT_RUNTIME := kryo300

# A/B
AB_OTA_UPDATER := true
AB_OTA_PARTITIONS := \
    boot \
    dtbo \
    init_boot \
    odm \
    product \
    recovery \
    system \
    system_dlkm \
    system_ext \
    vbmeta \
    vbmeta_system \
    vendor \
    vendor_boot \
    vendor_dlkm

# Bootloader
TARGET_BOARD_INFO_FILE := $(DEVICE_PATH)/configs/board-info.txt
TARGET_BOOTLOADER_BOARD_NAME := peridot

# Build
BUILD_BROKEN_DUP_RULES := true
BUILD_BROKEN_DUP_SYSPROP := true
BUILD_BROKEN_ELF_PREBUILT_PRODUCT_COPY_FILES := true
BUILD_BROKEN_VENDOR_PROPERTY_NAMESPACE := true

# DTB
BOARD_BOOT_HEADER_VERSION := 4
BOARD_MKBOOTIMG_ARGS += --header_version $(BOARD_BOOT_HEADER_VERSION)
BOARD_INIT_BOOT_HEADER_VERSION := 4
BOARD_MKBOOTIMG_INIT_ARGS += --header_version $(BOARD_INIT_BOOT_HEADER_VERSION)

# Filesystem
TARGET_FS_CONFIG_GEN := $(DEVICE_PATH)/configs/config.fs

# Init
TARGET_INIT_VENDOR_LIB := //$(DEVICE_PATH):libinit_peridot
TARGET_RECOVERY_DEVICE_MODULES := libinit_peridot

# Kernel
BOARD_KERNEL_CMDLINE := \
    video=vfb:640x400,bpp=32,memsize=3072000 \
    swinfo.fingerprint=peridot:$(AOSPA_VERSION) \
    mtdoops.fingerprint=peridot:$(AOSPA_VERSION)

# TODO: Delete after confirming that the sepolicy rules allow switching to Enforcing.
BOARD_KERNEL_CMDLINE += \
    androidboot.selinux=permissive

BOARD_BOOTCONFIG := \
    androidboot.hardware=qcom \
    androidboot.hypervisor.protected_vm.supported=0 \
    androidboot.load_modules_parallel=true \
    androidboot.memcg=1 \
    androidboot.serialconsole=0 \
    androidboot.usbcontroller=a600000.dwc3 \
    androidboot.vendor.qspa=true

BOARD_KERNEL_PAGESIZE := 4096
BOARD_INCLUDE_DTB_IN_BOOTIMG := true
BOARD_RAMDISK_USE_LZ4 := true
BOARD_USES_GENERIC_KERNEL_IMAGE := true
TARGET_HAS_GENERIC_KERNEL_HEADERS := true

# Partition
BOARD_FLASH_BLOCK_SIZE := 131072 # (BOARD_KERNEL_PAGESIZE * 64)
BOARD_BOOTIMAGE_PARTITION_SIZE := 100663296
BOARD_INIT_BOOT_IMAGE_PARTITION_SIZE := 8388608
BOARD_VENDOR_BOOTIMAGE_PARTITION_SIZE := 100663296
BOARD_DTBOIMG_PARTITION_SIZE := 25165824
BOARD_RECOVERYIMAGE_PARTITION_SIZE := 104857600
BOARD_USES_METADATA_PARTITION := true
BOARD_USES_VENDOR_DLKMIMAGE := true

BOARD_SUPER_PARTITION_SIZE ?= 9126805504
BOARD_SUPER_PARTITION_GROUPS := qti_dynamic_partitions
BOARD_QTI_DYNAMIC_PARTITIONS_PARTITION_LIST := odm product system system_dlkm system_ext vendor vendor_dlkm
BOARD_QTI_DYNAMIC_PARTITIONS_SIZE ?= 9122611200 # (BOARD_SUPER_PARTITION_SIZE - 4MB overhead)

$(foreach p, $(call to-upper, $(BOARD_QTI_DYNAMIC_PARTITIONS_PARTITION_LIST)), \
    $(if $(filter user,$(TARGET_BUILD_VARIANT)), \
        $(eval BOARD_$(p)IMAGE_FILE_SYSTEM_TYPE := erofs), \
        $(eval BOARD_$(p)IMAGE_FILE_SYSTEM_TYPE := ext4) \
        $(eval BOARD_$(p)IMAGE_PARTITION_RESERVED_SIZE := 104857600) \
    ) \
    $(eval TARGET_COPY_OUT_$(p) := $(call to-lower, $(p))) \
)

# Properties
TARGET_ODM_PROP += \
    $(DEVICE_PATH)/configs/properties/odm.prop

TARGET_PRODUCT_PROP += \
    $(DEVICE_PATH)/configs/properties/product.prop

TARGET_SYSTEM_PROP += \
    $(DEVICE_PATH)/configs/properties/system.prop

TARGET_SYSTEM_EXT_PROP += \
    $(DEVICE_PATH)/configs/properties/system_ext.prop

TARGET_VENDOR_PROP += \
    $(DEVICE_PATH)/configs/properties/vendor.prop

# Recovery
BOARD_EXCLUDE_KERNEL_FROM_RECOVERY_IMAGE := true
BOARD_USES_FULL_RECOVERY_IMAGE := true
TARGET_RECOVERY_FSTAB := $(DEVICE_PATH)/init/fstab.qcom
TARGET_RECOVERY_PIXEL_FORMAT := RGBX_8888
TARGET_RECOVERY_UI_MARGIN_HEIGHT := 104
TARGET_USERIMAGES_USE_F2FS := true

# UFS
#namespace definition for librecovery_updater
#differentiate legacy 'sg' or 'bsg' framework
SOONG_CONFIG_NAMESPACES += ufsbsg
SOONG_CONFIG_ufsbsg += ufsframework
SOONG_CONFIG_ufsbsg_ufsframework := bsg

# Verified Boot
BOARD_AVB_ENABLE := true
BOARD_AVB_MAKE_VBMETA_IMAGE_ARGS += --flags 3
BOARD_AVB_ALGORITHM := SHA256_RSA2048
BOARD_AVB_KEY_PATH := external/avb/test/data/testkey_rsa2048.pem
BOARD_MOVE_GSI_AVB_KEYS_TO_VENDOR_BOOT := true

BOARD_AVB_BOOT_KEY_PATH := external/avb/test/data/testkey_rsa2048.pem
BOARD_AVB_BOOT_ALGORITHM := SHA256_RSA2048
BOARD_AVB_BOOT_ROLLBACK_INDEX := $(PLATFORM_SECURITY_PATCH_TIMESTAMP)
BOARD_AVB_BOOT_ROLLBACK_INDEX_LOCATION := 3

BOARD_AVB_RECOVERY_KEY_PATH := external/avb/test/data/testkey_rsa2048.pem
BOARD_AVB_RECOVERY_ALGORITHM := SHA256_RSA2048
BOARD_AVB_RECOVERY_ROLLBACK_INDEX := $(PLATFORM_SECURITY_PATCH_TIMESTAMP)
BOARD_AVB_RECOVERY_ROLLBACK_INDEX_LOCATION := 1

BOARD_AVB_VBMETA_SYSTEM := system system_dlkm system_ext product
BOARD_AVB_VBMETA_SYSTEM_KEY_PATH := external/avb/test/data/testkey_rsa2048.pem
BOARD_AVB_VBMETA_SYSTEM_ALGORITHM := SHA256_RSA2048
BOARD_AVB_VBMETA_SYSTEM_ROLLBACK_INDEX := $(PLATFORM_SECURITY_PATCH_TIMESTAMP)
BOARD_AVB_VBMETA_SYSTEM_ROLLBACK_INDEX_LOCATION := 2

BOARD_AVB_VENDOR_DLKM_ADD_HASHTREE_FOOTER_ARGS += --hash_algorithm sha256
BOARD_AVB_VENDOR_ADD_HASHTREE_FOOTER_ARGS += --hash_algorithm sha256
BOARD_AVB_SYSTEM_DLKM_ADD_HASHTREE_FOOTER_ARGS += --hash_algorithm sha256

# VINTF
DEVICE_FRAMEWORK_COMPATIBILITY_MATRIX_FILE += \
    $(DEVICE_PATH)/configs/vintf/device_framework_matrix.xml \
    $(HARDWARE_PATH)/vintf/xiaomi_framework_compatibility_matrix.xml

DEVICE_FRAMEWORK_MANIFEST_FILE := \
    $(DEVICE_PATH)/configs/vintf/framework_manifest.xml

DEVICE_MANIFEST_FILE += \
    $(DEVICE_PATH)/configs/vintf/manifest_vendor.xml \
    $(AUDIO_HAL_DIR)/configs/common/manifest_non_qmaa.xml \
    $(AUDIO_HAL_DIR)/configs/common/manifest_non_qmaa_extn.xml

ODM_MANIFEST_FILES += \
    $(DEVICE_PATH)/configs/vintf/manifest_odm.xml

# WLAN
TARGET_WLAN_CHIP := qca6750
include device/qcom/wlan/pineapple/BoardConfigWlan.mk
