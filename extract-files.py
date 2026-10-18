#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/peridot',
    'hardware/xiaomi',
    'vendor/qcom/common/system/av',
    'vendor/qcom/common/system/display',
    'vendor/qcom/common/system/perf',
    'vendor/qcom/common/vendor/perf',
    'vendor/qcom/common/vendor/adreno/u',
    'vendor/qcom/common/vendor/display/6.1',
    'vendor/qcom/common/vendor/media/6.1',
]

def lib_fixup_odm_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'odm' else None

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_vendor'

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'sqlite3',
        'libqshcamera',
    ): lib_fixup_odm_suffix,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'com.qualcomm.qti.imscmservice@2.0',
        'com.qualcomm.qti.imscmservice@2.1',
        'com.qualcomm.qti.imscmservice@2.2',
        'com.qualcomm.qti.uceservice@2.0',
        'com.qualcomm.qti.uceservice@2.1',
        'com.qualcomm.qti.uceservice@2.2',
        'com.qualcomm.qti.uceservice@2.3',
        'vendor.qti.ImsRtpService-V1-ndk',
        'vendor.qti.data.factoryservice-V1-ndk',
        'vendor.qti.data.mwqem@1.0',
        'vendor.qti.data.mwqemaidlservice-V1-ndk',
        'vendor.qti.data.slm@1.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.data.cneaidlservice.internal.api-V1-ndk',
        'vendor.qti.hardware.data.cneaidlservice.internal.constants-V1-ndk',
        'vendor.qti.hardware.data.cneaidlservice.internal.server-V1-ndk',
        'vendor.qti.hardware.data.connection@1.0',
        'vendor.qti.hardware.data.connection@1.1',
        'vendor.qti.hardware.data.connectionfactory-V1-ndk',
        'vendor.qti.hardware.data.dataactivity-V1-ndk',
        'vendor.qti.hardware.data.dynamicdds@1.0',
        'vendor.qti.hardware.data.dynamicdds@1.1',
        'vendor.qti.hardware.data.dynamicddsaidlservice-V1-ndk',
        'vendor.qti.hardware.data.flow@1.0',
        'vendor.qti.hardware.data.flow@1.1',
        'vendor.qti.hardware.data.flowaidlservice-V1-ndk',
        'vendor.qti.hardware.data.iwlandata-V1-ndk',
        'vendor.qti.hardware.data.ka-V1-ndk',
        'vendor.qti.hardware.data.latency@1.0',
        'vendor.qti.hardware.data.lce@1.0',
        'vendor.qti.hardware.data.lceaidlservice-V1-ndk',
        'vendor.qti.hardware.data.qmiaidlservice-V1-ndk',
        'vendor.qti.hardware.ListenSoundModel@1.0',
        'vendor.qti.hardware.dpmaidlservice-V1-ndk',
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.hardware.dpmservice@1.1',
        'vendor.qti.hardware.mwqemadapter@1.0',
        'vendor.qti.hardware.mwqemadapteraidlservice-V1-ndk',
        'vendor.qti.hardware.qccsyshal@1.0',
        'vendor.qti.hardware.qccsyshal@1.1',
        'vendor.qti.hardware.qccsyshal@1.2',
        'vendor.qti.hardware.radio.am@1.0',
        'vendor.qti.hardware.radio.ims@1.0',
        'vendor.qti.hardware.radio.ims@1.1',
        'vendor.qti.hardware.radio.ims@1.2',
        'vendor.qti.hardware.radio.ims@1.3',
        'vendor.qti.hardware.radio.ims@1.4',
        'vendor.qti.hardware.radio.ims@1.5',
        'vendor.qti.hardware.radio.ims@1.6',
        'vendor.qti.hardware.radio.ims@1.7',
        'vendor.qti.hardware.radio.ims@1.8',
        'vendor.qti.hardware.radio.lpa@1.0',
        'vendor.qti.hardware.radio.lpa@1.1',
        'vendor.qti.hardware.radio.lpa@1.2',
        'vendor.qti.hardware.radio.qcrilhook@1.0',
        'vendor.qti.hardware.radio.qtiradio@1.0',
        'vendor.qti.hardware.radio.qtiradio@2.0',
        'vendor.qti.hardware.radio.qtiradio@2.1',
        'vendor.qti.hardware.radio.qtiradio@2.2',
        'vendor.qti.hardware.radio.qtiradio@2.3',
        'vendor.qti.hardware.radio.qtiradio@2.4',
        'vendor.qti.hardware.radio.qtiradio@2.5',
        'vendor.qti.hardware.radio.qtiradio@2.6',
        'vendor.qti.hardware.radio.uim@1.0',
        'vendor.qti.hardware.radio.uim@1.1',
        'vendor.qti.hardware.radio.uim@1.2',
        'vendor.qti.hardware.radio.uim_remote_client@1.0',
        'vendor.qti.hardware.radio.uim_remote_client@1.1',
        'vendor.qti.hardware.radio.uim_remote_client@1.2',
        'vendor.qti.hardware.radio.uim_remote_server@1.0',
        'vendor.qti.hardware.slmadapter@1.0',
        'vendor.qti.hardware.vpp-V1-ndk',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.ims.callcapability@1.0',
        'vendor.qti.ims.callcapabilityaidlservice-V1-ndk',
        'vendor.qti.ims.callinfo@1.0',
        'vendor.qti.ims.configaidlservice-V1-ndk',
        'vendor.qti.ims.connectionaidlservice-V1-ndk',
        'vendor.qti.ims.factory@1.0',
        'vendor.qti.ims.factory@1.1',
        'vendor.qti.ims.factoryaidlservice-V1-ndk',
        'vendor.qti.ims.rcsconfig@1.0',
        'vendor.qti.ims.rcsconfig@1.1',
        'vendor.qti.ims.rcsconfig@2.0',
        'vendor.qti.ims.rcsconfig@2.1',
        'vendor.qti.ims.rcssipaidlservice-V1-ndk',
        'vendor.qti.ims.rcsuceaidlservice-V1-ndk',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.imsrtpservice@3.1',
        'vendor.qti.latency@2.0',
        'vendor.qti.latency@2.1',
        'vendor.qti.latency@2.2',
        'vendor.qti.latencyaidlservice-V1-ndk',
        'vendor.qti.qccvndhal_aidl-V1-ndk',
        ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'odm/lib64/anc.hal.so': blob_fixup()
        .add_needed('libion.so'),
    'system_ext/etc/init/qspa_system.rc': blob_fixup()
        .regex_replace(r'\$\{ro\.boot\.vendor\.qspa:-default\}', 'default'),
    'system_ext/etc/vintf/manifest/vendor.qti.qesdsys.service.xml': blob_fixup()
        .regex_replace(r'(?s)^.*?(?=<manifest)', ''),
    'system_ext/lib64/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so')
        .remove_needed('android.hidl.base@1.0.so'),
    'system_ext/lib64/vendor.qti.hardware.qccsyshal@1.2-halimpl.so': blob_fixup()
        .replace_needed(
            'libprotobuf-cpp-full.so',
            'libprotobuf-cpp-full-21.7.so'
    ),
    (
        'odm/lib64/camera/plugins/com.xiaomi.plugin.anchor.so',
        'odm/lib64/com.qti.feature2.anchorsync.so',
        'vendor/bin/hw/vendor.qti.hardware.display.composer-service',
        'vendor/lib64/libaudiocloudctrl.so',
        'vendor/lib64/liblearningmodule.so',
    ): blob_fixup()
        .replace_needed(
            'libtinyxml2.so',
            'libtinyxml2-v34.so'
    ),
    (
        'odm/etc/camera/enhance_motiontuning.xml',
        'odm/etc/camera/motiontuning.xml',
        'odm/etc/camera/night_motiontuning.xml'
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),
    (
        'odm/lib64/camera/plugins/com.xiaomi.plugin.gainmap.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.jpegrAggr.so',
    ): blob_fixup()
        .replace_needed(
            'libultrahdr.so',
            'libultrahdr_prebuilt.so'
    ),
    (
        'odm/lib64/hw/camera.qcom.so',
        'odm/lib64/hw/com.qti.chi.override.so',
        'odm/lib64/libchifeature2.so',
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so'
    ),
    'odm/lib64/hw/camera.xiaomi.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so'
        )
        .replace_needed(
            'libtinyxml2.so',
            'libtinyxml2-v34.so'
    ),
    (
        'odm/lib64/camera/com.qti.actuator.peridot_aac_imx882_gt9764ber_wide_i_actuator.so',
        'odm/lib64/camera/com.qti.actuator.peridot_ofilm_imx882_aw86016csr_wide_ii_actuator.so',
        'odm/lib64/camera/com.qti.actuator.peridot_ofilm_imx882_gt9764ber_wide_iii_actuator.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_aac_imx355_gt24p64e_ultra_i_eeprom.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_aac_imx882_gt24p128f_wide_i_eeprom.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_aac_ov20b40_gt24p64e_front_ii_eeprom.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_ofilm_imx355_p24c64e_ultra_ii_eeprom.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_ofilm_imx882_bl24sa128b_wide_ii_eeprom.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_ofilm_imx882_gt24p128f_wide_iii_eeprom.so',
        'odm/lib64/camera/com.qti.eeprom.peridot_ofilm_ov20b40_p24c64e_front_eeprom.so',
        'odm/lib64/camera/com.qti.sensor.peridot_aac_imx355_ultra_i.so',
        'odm/lib64/camera/com.qti.sensor.peridot_aac_imx882_wide_i.so',
        'odm/lib64/camera/com.qti.sensor.peridot_ofilm_ov20b40_front.so',
        'odm/lib64/camera/components/com.jigan.node.videobokeh.so',
        'odm/lib64/camera/components/com.mi.node.aiasd.so',
        'odm/lib64/camera/components/com.mi.node.dlengine.so',
        'odm/lib64/camera/components/com.mi.node.mawsaliency.so',
        'odm/lib64/camera/components/com.mi.node.skinbeautifier.so',
        'odm/lib64/camera/components/com.mi.node.videobokeh.so',
        'odm/lib64/camera/components/com.mi.node.videofilter.so',
        'odm/lib64/camera/components/com.mi.node.videonight.so',
        'odm/lib64/camera/components/com.qti.hwcfg.bps.so',
        'odm/lib64/camera/components/com.qti.hwcfg.ife.so',
        'odm/lib64/camera/components/com.qti.hwcfg.ipe.so',
        'odm/lib64/camera/components/com.qti.node.aon.so',
        'odm/lib64/camera/components/com.qti.node.depth.so',
        'odm/lib64/camera/components/com.qti.node.depthprovider.so',
        'odm/lib64/camera/components/com.qti.node.dewarp.so',
        'odm/lib64/camera/components/com.qti.node.eisv2.so',
        'odm/lib64/camera/components/com.qti.node.eisv3.so',
        'odm/lib64/camera/components/com.qti.node.evadepth.so',
        'odm/lib64/camera/components/com.qti.node.gme.so',
        'odm/lib64/camera/components/com.qti.node.gyrornn.so',
        'odm/lib64/camera/components/com.qti.node.hdr10pgen.so',
        'odm/lib64/camera/components/com.qti.node.hdr10phist.so',
        'odm/lib64/camera/components/com.qti.node.itofpreprocess.so',
        'odm/lib64/camera/components/com.qti.node.ml.so',
        'odm/lib64/camera/components/com.qti.node.mlinference.so',
        'odm/lib64/camera/components/com.qti.node.pixelstats.so',
        'odm/lib64/camera/components/com.qti.node.seg.so',
        'odm/lib64/camera/components/com.qti.node.swec.so',
        'odm/lib64/camera/components/com.qti.node.swregistration.so',
        'odm/lib64/camera/components/com.qti.stats.cnndriver.so',
        'odm/lib64/camera/components/libcamxevainterface.so',
        'odm/lib64/camera/components/libdepthmapwrapper_itof.so',
        'odm/lib64/camera/components/libdepthmapwrapper_secure.so',
        'odm/lib64/camera/libchxlogicalcameratable.so',
        'odm/lib64/com.qti.camx.chiiqutils.so',
        'odm/lib64/com.qti.chiusecaseselector.so',
        'odm/lib64/com.qti.feature2.afbrckt.so',
        'odm/lib64/com.qti.feature2.demux.so',
        'odm/lib64/com.qti.feature2.derivedoffline.so',
        'odm/lib64/com.qti.feature2.fusion.so',
        'odm/lib64/com.qti.feature2.generic.so',
        'odm/lib64/com.qti.feature2.gs.sm8650.so',
        'odm/lib64/com.qti.feature2.hdr.so',
        'odm/lib64/com.qti.feature2.mcreprocrt.so',
        'odm/lib64/com.qti.feature2.memcpy.so',
        'odm/lib64/com.qti.feature2.metadataserializer.so',
        'odm/lib64/com.qti.feature2.mfsr.so',
        'odm/lib64/com.qti.feature2.ml.so',
        'odm/lib64/com.qti.feature2.mux.so',
        'odm/lib64/com.qti.feature2.offlinestatsregeneration.so',
        'odm/lib64/com.qti.feature2.qcfa.so',
        'odm/lib64/com.qti.feature2.rawhdr.so',
        'odm/lib64/com.qti.feature2.realtimeserializer.so',
        'odm/lib64/com.qti.feature2.rt.so',
        'odm/lib64/com.qti.feature2.rtmcx.so',
        'odm/lib64/com.qti.feature2.serializer.so',
        'odm/lib64/com.qti.feature2.statsregeneration.so',
        'odm/lib64/com.qti.feature2.stub.so',
        'odm/lib64/com.qti.feature2.swmf.so',
        'odm/lib64/com.qti.qseeutils.so',
        'odm/lib64/com.qualcomm.mcx.distortionmapper.so',
        'odm/lib64/com.qualcomm.mcx.linearmapper.so',
        'odm/lib64/com.qualcomm.mcx.nonlinearmapper.so',
        'odm/lib64/com.qualcomm.mcx.policy.mfl.so',
        'odm/lib64/com.qualcomm.qti.mcx.usecase.extension.so',
        'odm/lib64/com.xiaomi.camx.hook.so',
        'odm/lib64/com.xiaomi.chi.hook.so',
        'odm/lib64/hw/camera.qcom.sm8650.so',
        'odm/lib64/hw/com.qti.chi.offline.so',
        'odm/lib64/libcamerapostproc.so',
        'odm/lib64/libcamxhwnodecontext.so',
        'odm/lib64/libcamxifestriping.so',
        'odm/lib64/libcamximageformatutils.so',
        'odm/lib64/libcamxncsdatafactory.so',
        'odm/lib64/libcom.xiaomi.mawutilsold.so',
        'odm/lib64/libcommonchiutils.so',
        'odm/lib64/libfastmessage.so',
        'odm/lib64/libhme.so',
        'odm/lib64/libipebpsstriping.so',
        'odm/lib64/libipebpsstriping170.so',
        'odm/lib64/libipebpsstriping480.so',
        'odm/lib64/libisphwsetting.so',
        'odm/lib64/libjpege.so',
        'odm/lib64/libmctfengine_stub.so',
        'odm/lib64/libmfec.so',
        'odm/lib64/libmmcamera_bestats.so',
        'odm/lib64/libmmcamera_cac.so',
        'odm/lib64/libmmcamera_lscv35.so',
        'odm/lib64/libmmcamera_pdpc.so',
        'odm/lib64/libofflinefeatureintf.so',
        'odm/lib64/libopestriping.so',
        'odm/lib64/libtfestriping.so',
        'odm/lib64/libubifocus.so',
        'odm/lib64/vendor.qti.hardware.camera.aon-service-impl.so',
        'odm/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
        'odm/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so'
    ),
    'odm/lib64/com.qti.feature2.anchorsync.so': blob_fixup()
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so'
        )
        .replace_needed(
            'libtinyxml2.so',
            'libtinyxml2-v34.so'
    ),
    (
        'odm/lib64/libcamxcommonutils.so',
        'odm/lib64/libmialgoengine.so',
        'vendor/lib64/libcameraopt.so',
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    (
        'odm/lib64/libAncHumanVideoBokehV4.so',
        'odm/lib64/libTrueSight.so',
        'odm/lib64/libMiPhotoFilter.so',
        'odm/lib64/libwa_widelens_undistort.so',
        'odm/lib64/libmorpho_ubwc.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_isSupported')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'odm/lib64/libsnpe_config.so': blob_fixup()
        .add_needed('liblog.so'),
    (
        'odm/lib64/libaudioroute_ext.so',
        'vendor/lib64/libagm.so',
        'vendor/lib64/libar-pal.so',
        'vendor/lib64/libkaraokepal.so',
        'vendor/lib64/libmcs.so',
    ): blob_fixup()
        .replace_needed(
            'libaudioroute.so',
            'libaudioroute-v34.so'
    ),
    'vendor/etc/clstc_config_library.xml': blob_fixup()
        .regex_replace(r'<library>\s*<name>libdolbyclstc[\s\S]*?</library>', ''),
    'vendor/etc/seccomp_policy/c2audio.vendor.ext-arm64.policy': blob_fixup()
        .add_line_if_missing('setsockopt: 1'),
    'vendor/etc/vintf/manifest/c2_manifest_vendor.xml': blob_fixup()
        .regex_replace('.+DOLBY.+\n', ''),
    (
        'vendor/bin/qcc-vendor',
        'vendor/bin/qms',
        'vendor/bin/xtra-daemon',
        'vendor/lib64/libcne.so',
        'vendor/lib64/libqcc_sdk.so',
        'vendor/lib64/libqms_client.so',
    ): blob_fixup()
        .add_needed('libbinder_shim.so'),
    'vendor/lib64/libqcodec2_core.so': blob_fixup()
        .add_needed('libcodec2_shim.so'),
    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed('libbinder_shim.so')
        .add_needed('libhidlbase_shim.so'),
    'vendor/lib64/libultrahdr_prebuilt.so': blob_fixup()
        .replace_needed(
            'libjpegdecoder.so',
            'libjpegdecoder_prebuilt.so'
        )
        .replace_needed(
            'libjpegencoder.so',
            'libjpegencoder_prebuilt.so'
    ),
    (
        'vendor/lib64/libVoiceSdk.so',
        'vendor/lib64/libcapiv2uvvendor.so',
        'vendor/lib64/liblistensoundmodel2vendor.so',
    ): blob_fixup()
        .replace_needed(
            'libtensorflowlite_c.so',
            'libtensorflowlite_c_vendor.so',
    ),
}  # fmt: skip

module = ExtractUtilsModule(
    'peridot',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
