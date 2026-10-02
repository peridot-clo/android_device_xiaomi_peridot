#
# Copyright (C) 2026 Project Mia
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/aosp_base_telephony.mk)

# Inherit from the device configuration.
$(call inherit-product, device/xiaomi/peridot/pineapple.mk)

# Inherit from the Mia configuration.
$(call inherit-product, vendor/mia/target/product/mobile.mk)

# Boot animation resolution.

# Boot animation resolution.
TARGET_BOOT_ANIMATION_RES := 1440

PRODUCT_NAME := mia_peridot
PRODUCT_DEVICE := peridot
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 24069RA21C

PRODUCT_SYSTEM_NAME := peridot
PRODUCT_SYSTEM_DEVICE := peridot

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="peridot-user 16 BP2A.250605.031.A3 OS3.0.305.0.WNPCNXM release-keys" \
    BuildFingerprint=Redmi/peridot/peridot:16/BP2A.250605.031.A3/OS3.0.305.0.WNPCNXM:user/release-keys \
    DeviceName=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
