# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/localonly.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic.PbDefinitions import config_pb2 as meshtastic_dot_config__pb2
from meshtastic.PbDefinitions import module_config_pb2 as meshtastic_dot_module__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ameshtastic/localonly.proto\x12\nmeshtastic\x1a\x17meshtastic/config.proto\x1a\x1emeshtastic/module_config.proto\"\xfd\x02\n\x0bLocalConfig\x12/\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x1f.meshtastic.Config.DeviceConfig\x12\x33\n\x08position\x18\x02 \x01(\x0b\x32!.meshtastic.Config.PositionConfig\x12-\n\x05power\x18\x03 \x01(\x0b\x32\x1e.meshtastic.Config.PowerConfig\x12\x31\n\x07network\x18\x04 \x01(\x0b\x32 .meshtastic.Config.NetworkConfig\x12\x31\n\x07\x64isplay\x18\x05 \x01(\x0b\x32 .meshtastic.Config.DisplayConfig\x12+\n\x04lora\x18\x06 \x01(\x0b\x32\x1d.meshtastic.Config.LoRaConfig\x12\x35\n\tbluetooth\x18\x07 \x01(\x0b\x32\".meshtastic.Config.BluetoothConfig\x12\x0f\n\x07version\x18\x08 \x01(\r\"\xfb\x06\n\x11LocalModuleConfig\x12\x31\n\x04mqtt\x18\x01 \x01(\x0b\x32#.meshtastic.ModuleConfig.MQTTConfig\x12\x35\n\x06serial\x18\x02 \x01(\x0b\x32%.meshtastic.ModuleConfig.SerialConfig\x12R\n\x15\x65xternal_notification\x18\x03 \x01(\x0b\x32\x33.meshtastic.ModuleConfig.ExternalNotificationConfig\x12\x42\n\rstore_forward\x18\x04 \x01(\x0b\x32+.meshtastic.ModuleConfig.StoreForwardConfig\x12<\n\nrange_test\x18\x05 \x01(\x0b\x32(.meshtastic.ModuleConfig.RangeTestConfig\x12;\n\ttelemetry\x18\x06 \x01(\x0b\x32(.meshtastic.ModuleConfig.TelemetryConfig\x12\x44\n\x0e\x63\x61nned_message\x18\x07 \x01(\x0b\x32,.meshtastic.ModuleConfig.CannedMessageConfig\x12\x33\n\x05\x61udio\x18\t \x01(\x0b\x32$.meshtastic.ModuleConfig.AudioConfig\x12\x46\n\x0fremote_hardware\x18\n \x01(\x0b\x32-.meshtastic.ModuleConfig.RemoteHardwareConfig\x12\x42\n\rneighbor_info\x18\x0b \x01(\x0b\x32+.meshtastic.ModuleConfig.NeighborInfoConfig\x12H\n\x10\x61mbient_lighting\x18\x0c \x01(\x0b\x32..meshtastic.ModuleConfig.AmbientLightingConfig\x12H\n\x10\x64\x65tection_sensor\x18\r \x01(\x0b\x32..meshtastic.ModuleConfig.DetectionSensorConfig\x12=\n\npaxcounter\x18\x0e \x01(\x0b\x32).meshtastic.ModuleConfig.PaxcounterConfig\x12\x0f\n\x07version\x18\x08 \x01(\rBd\n\x13\x63om.geeksville.meshB\x0fLocalOnlyProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.localonly_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\017LocalOnlyProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _LOCALCONFIG._serialized_start=100
  _LOCALCONFIG._serialized_end=481
  _LOCALMODULECONFIG._serialized_start=484
  _LOCALMODULECONFIG._serialized_end=1375
# @@protoc_insertion_point(module_scope)
