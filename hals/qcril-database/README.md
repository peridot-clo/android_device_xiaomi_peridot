# Peridot QCRIL database

This device database packaging follows:
https://github.com/LineageOS/android_device_xiaomi_peridot/tree/lineage-23.2/qcril-database

The device packages a generated `qcrilNr.db` together with the 15.1 configuration upgrade. Generation uses the extracted Peridot SQL inputs, preserving the matching Qualcomm module definitions, emergency-number tables and configuration defaults. The additional configuration sets the database version to 15.1 and the default `persist.vendor.radio.poweron_opt` to 0.

The host generator is adapted from LineageOS/android_hardware_qcom-caf_common at 5cd53603d36aaddd9ba9d882dad5411f1b30fbed, qcril-database/generate_qcril_db.py. Its SQL ordering is unchanged: version-sorted main scripts, then version-sorted configuration scripts. Local output-path validation protects existing files outside the build directory. Keeping this small host tool device-local avoids changing the AOSPA common tree.

The captured R3 installation had an empty MODULES table, no CONFIGS or CONFIG_MODULES tables, an unloaded libqcrilDataModule.so in both qcril processes, and repeated Phone startup ANRs in RIL.getRadioServiceProxy waiting for the declared IRadioData/slot1 instance. The real plugin and its dependencies were present; a 131-library audit found no unresolved strong symbols. The new database must contain all 28 matching module definitions and select DataModule 16 in the Full configuration.

Build-time database integrity, version, module selection and target-files membership are required checks. Runtime acceptance still requires both native AIDL Radio Data instances to register and Phone to remain stable without startup ANRs. Do not remove the manifest declaration, replace the native provider with a dummy service, clear user radio databases, or raise timeouts to conceal the failure.
