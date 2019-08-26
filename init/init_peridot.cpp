/*
 * Copyright (c) 2021, The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <android-base/properties.h>
#define _REALLY_INCLUDE_SYS__SYSTEM_PROPERTIES_H_
#include <sys/_system_properties.h>

#include "vendor_init.h"
#include "property_service.h"

void property_override(char const prop[], char const value[]) {
    prop_info *pi;

    pi = (prop_info*) __system_property_find(prop);

    if (pi)
        __system_property_update(pi, value, strlen(value));
    else
        __system_property_add(prop, strlen(prop), value, strlen(value));
}

void load_peridot() {
    property_override("bluetooth.device.default_name", "Redmi Turbo 3");
    property_override("ro.product.odm.name", "peridot");
    property_override("ro.product.odm.model", "24069RA21C");
    property_override("vendor.usb.product_string", "Redmi Turbo 3");
}

void load_peridot_global() {
    property_override("bluetooth.device.default_name", "POCO F6");
    property_override("ro.product.odm.model", "24069PC21G");
    property_override("ro.product.odm.name", "peridot_global");
    property_override("vendor.usb.product_string", "POCO F6");
}

void load_peridot_india() {
    property_override("bluetooth.device.default_name", "POCO F6");
    property_override("ro.product.odm.model", "24069PC21I");
    property_override("ro.product.odm.name", "peridot_in");
    property_override("vendor.usb.product_string", "POCO F6");
}

void vendor_load_properties() {
    std::string region = android::base::GetProperty("ro.boot.hwc", "");

    if (region.find("CN") != std::string::npos)
        load_peridot();
    else if (region.find("INDIA") != std::string::npos)
        load_peridot_india();
    else if (region.find("GLOBAL") != std::string::npos)
        load_peridot_global();
}
