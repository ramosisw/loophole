# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exercise_laps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exercise_laps.proto',
  package='data',
  serialized_pb=_b('\n\x13\x65xercise_laps.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"\x99\x02\n\x0bPbLapHeader\x12\x1f\n\nsplit_time\x18\x01 \x02(\x0b\x32\x0b.PbDuration\x12\x1d\n\x08\x64uration\x18\x02 \x02(\x0b\x32\x0b.PbDuration\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\x12\x0e\n\x06\x61scent\x18\x04 \x01(\x02\x12\x0f\n\x07\x64\x65scent\x18\x05 \x01(\x02\x12\x35\n\x0c\x61utolap_type\x18\x06 \x01(\x0e\x32\x1f.data.PbLapHeader.PbAutolapType\"`\n\rPbAutolapType\x12\x19\n\x15\x41UTOLAP_TYPE_DISTANCE\x10\x01\x12\x19\n\x15\x41UTOLAP_TYPE_DURATION\x10\x02\x12\x19\n\x15\x41UTOLAP_TYPE_LOCATION\x10\x03\"`\n\x17PbLapSwimmingStatistics\x12\x13\n\x0blap_strokes\x18\x01 \x01(\r\x12\x12\n\npool_count\x18\x02 \x01(\r\x12\x1c\n\x14\x61vg_duration_of_pool\x18\x03 \x01(\x02\"M\n\x18PbLapHeartRateStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\x12\x0f\n\x07maximum\x18\x02 \x01(\r\x12\x0f\n\x07minimum\x18\x03 \x01(\r\"8\n\x14PbLapSpeedStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\x12\x0f\n\x07maximum\x18\x02 \x01(\x02\":\n\x16PbLapCadenceStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\x12\x0f\n\x07maximum\x18\x02 \x01(\r\"8\n\x14PbLapPowerStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x05\x12\x0f\n\x07maximum\x18\x02 \x01(\x05\"+\n\x18PbLapLRBalanceStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\"/\n\x1cPbLapPedalingIndexStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\"4\n!PbLapPedalingEfficiencyStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\"%\n\x16PbLapInclineStatistics\x12\x0b\n\x03max\x18\x01 \x01(\x02\".\n\x1bPbLapStrideLengthStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\"\xf0\x03\n\x0fPbLapStatistics\x12\x32\n\nheart_rate\x18\x01 \x01(\x0b\x32\x1e.data.PbLapHeartRateStatistics\x12)\n\x05speed\x18\x02 \x01(\x0b\x32\x1a.data.PbLapSpeedStatistics\x12-\n\x07\x63\x61\x64\x65nce\x18\x03 \x01(\x0b\x32\x1c.data.PbLapCadenceStatistics\x12)\n\x05power\x18\x04 \x01(\x0b\x32\x1a.data.PbLapPowerStatistics\x12\x43\n\x17OBSOLETE_pedaling_index\x18\x05 \x01(\x0b\x32\".data.PbLapPedalingIndexStatistics\x12-\n\x07incline\x18\x06 \x01(\x0b\x32\x1c.data.PbLapInclineStatistics\x12\x38\n\rstride_length\x18\x07 \x01(\x0b\x32!.data.PbLapStrideLengthStatistics\x12:\n\x13swimming_statistics\x18\x08 \x01(\x0b\x32\x1d.data.PbLapSwimmingStatistics\x12:\n\x12left_right_balance\x18\t \x01(\x0b\x32\x1e.data.PbLapLRBalanceStatistics\"U\n\x05PbLap\x12!\n\x06header\x18\x01 \x02(\x0b\x32\x11.data.PbLapHeader\x12)\n\nstatistics\x18\x02 \x01(\x0b\x32\x15.data.PbLapStatistics\"a\n\x0cPbLapSummary\x12&\n\x11\x62\x65st_lap_duration\x18\x01 \x01(\x0b\x32\x0b.PbDuration\x12)\n\x14\x61verage_lap_duration\x18\x02 \x01(\x0b\x32\x0b.PbDuration\"H\n\x06PbLaps\x12\x19\n\x04laps\x18\x01 \x03(\x0b\x32\x0b.data.PbLap\x12#\n\x07summary\x18\x02 \x01(\x0b\x32\x12.data.PbLapSummary\"P\n\nPbAutoLaps\x12\x1d\n\x08\x61utoLaps\x18\x01 \x03(\x0b\x32\x0b.data.PbLap\x12#\n\x07summary\x18\x02 \x01(\x0b\x32\x12.data.PbLapSummary')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PBLAPHEADER_PBAUTOLAPTYPE = _descriptor.EnumDescriptor(
  name='PbAutolapType',
  full_name='data.PbLapHeader.PbAutolapType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTOLAP_TYPE_DISTANCE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOLAP_TYPE_DURATION', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOLAP_TYPE_LOCATION', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=228,
  serialized_end=324,
)
_sym_db.RegisterEnumDescriptor(_PBLAPHEADER_PBAUTOLAPTYPE)


_PBLAPHEADER = _descriptor.Descriptor(
  name='PbLapHeader',
  full_name='data.PbLapHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='split_time', full_name='data.PbLapHeader.split_time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='data.PbLapHeader.duration', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='data.PbLapHeader.distance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ascent', full_name='data.PbLapHeader.ascent', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='descent', full_name='data.PbLapHeader.descent', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autolap_type', full_name='data.PbLapHeader.autolap_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBLAPHEADER_PBAUTOLAPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=324,
)


_PBLAPSWIMMINGSTATISTICS = _descriptor.Descriptor(
  name='PbLapSwimmingStatistics',
  full_name='data.PbLapSwimmingStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lap_strokes', full_name='data.PbLapSwimmingStatistics.lap_strokes', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pool_count', full_name='data.PbLapSwimmingStatistics.pool_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avg_duration_of_pool', full_name='data.PbLapSwimmingStatistics.avg_duration_of_pool', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=422,
)


_PBLAPHEARTRATESTATISTICS = _descriptor.Descriptor(
  name='PbLapHeartRateStatistics',
  full_name='data.PbLapHeartRateStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapHeartRateStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbLapHeartRateStatistics.maximum', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum', full_name='data.PbLapHeartRateStatistics.minimum', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=501,
)


_PBLAPSPEEDSTATISTICS = _descriptor.Descriptor(
  name='PbLapSpeedStatistics',
  full_name='data.PbLapSpeedStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapSpeedStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbLapSpeedStatistics.maximum', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=559,
)


_PBLAPCADENCESTATISTICS = _descriptor.Descriptor(
  name='PbLapCadenceStatistics',
  full_name='data.PbLapCadenceStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapCadenceStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbLapCadenceStatistics.maximum', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=619,
)


_PBLAPPOWERSTATISTICS = _descriptor.Descriptor(
  name='PbLapPowerStatistics',
  full_name='data.PbLapPowerStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapPowerStatistics.average', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbLapPowerStatistics.maximum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=677,
)


_PBLAPLRBALANCESTATISTICS = _descriptor.Descriptor(
  name='PbLapLRBalanceStatistics',
  full_name='data.PbLapLRBalanceStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapLRBalanceStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=722,
)


_PBLAPPEDALINGINDEXSTATISTICS = _descriptor.Descriptor(
  name='PbLapPedalingIndexStatistics',
  full_name='data.PbLapPedalingIndexStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapPedalingIndexStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=771,
)


_PBLAPPEDALINGEFFICIENCYSTATISTICS = _descriptor.Descriptor(
  name='PbLapPedalingEfficiencyStatistics',
  full_name='data.PbLapPedalingEfficiencyStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapPedalingEfficiencyStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=773,
  serialized_end=825,
)


_PBLAPINCLINESTATISTICS = _descriptor.Descriptor(
  name='PbLapInclineStatistics',
  full_name='data.PbLapInclineStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max', full_name='data.PbLapInclineStatistics.max', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=864,
)


_PBLAPSTRIDELENGTHSTATISTICS = _descriptor.Descriptor(
  name='PbLapStrideLengthStatistics',
  full_name='data.PbLapStrideLengthStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLapStrideLengthStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=912,
)


_PBLAPSTATISTICS = _descriptor.Descriptor(
  name='PbLapStatistics',
  full_name='data.PbLapStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heart_rate', full_name='data.PbLapStatistics.heart_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='data.PbLapStatistics.speed', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cadence', full_name='data.PbLapStatistics.cadence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='data.PbLapStatistics.power', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_pedaling_index', full_name='data.PbLapStatistics.OBSOLETE_pedaling_index', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incline', full_name='data.PbLapStatistics.incline', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride_length', full_name='data.PbLapStatistics.stride_length', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swimming_statistics', full_name='data.PbLapStatistics.swimming_statistics', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_right_balance', full_name='data.PbLapStatistics.left_right_balance', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=1411,
)


_PBLAP = _descriptor.Descriptor(
  name='PbLap',
  full_name='data.PbLap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='data.PbLap.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='statistics', full_name='data.PbLap.statistics', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1413,
  serialized_end=1498,
)


_PBLAPSUMMARY = _descriptor.Descriptor(
  name='PbLapSummary',
  full_name='data.PbLapSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='best_lap_duration', full_name='data.PbLapSummary.best_lap_duration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_lap_duration', full_name='data.PbLapSummary.average_lap_duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1500,
  serialized_end=1597,
)


_PBLAPS = _descriptor.Descriptor(
  name='PbLaps',
  full_name='data.PbLaps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='laps', full_name='data.PbLaps.laps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary', full_name='data.PbLaps.summary', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1599,
  serialized_end=1671,
)


_PBAUTOLAPS = _descriptor.Descriptor(
  name='PbAutoLaps',
  full_name='data.PbAutoLaps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='autoLaps', full_name='data.PbAutoLaps.autoLaps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summary', full_name='data.PbAutoLaps.summary', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1673,
  serialized_end=1753,
)

_PBLAPHEADER.fields_by_name['split_time'].message_type = types_pb2._PBDURATION
_PBLAPHEADER.fields_by_name['duration'].message_type = types_pb2._PBDURATION
_PBLAPHEADER.fields_by_name['autolap_type'].enum_type = _PBLAPHEADER_PBAUTOLAPTYPE
_PBLAPHEADER_PBAUTOLAPTYPE.containing_type = _PBLAPHEADER
_PBLAPSTATISTICS.fields_by_name['heart_rate'].message_type = _PBLAPHEARTRATESTATISTICS
_PBLAPSTATISTICS.fields_by_name['speed'].message_type = _PBLAPSPEEDSTATISTICS
_PBLAPSTATISTICS.fields_by_name['cadence'].message_type = _PBLAPCADENCESTATISTICS
_PBLAPSTATISTICS.fields_by_name['power'].message_type = _PBLAPPOWERSTATISTICS
_PBLAPSTATISTICS.fields_by_name['OBSOLETE_pedaling_index'].message_type = _PBLAPPEDALINGINDEXSTATISTICS
_PBLAPSTATISTICS.fields_by_name['incline'].message_type = _PBLAPINCLINESTATISTICS
_PBLAPSTATISTICS.fields_by_name['stride_length'].message_type = _PBLAPSTRIDELENGTHSTATISTICS
_PBLAPSTATISTICS.fields_by_name['swimming_statistics'].message_type = _PBLAPSWIMMINGSTATISTICS
_PBLAPSTATISTICS.fields_by_name['left_right_balance'].message_type = _PBLAPLRBALANCESTATISTICS
_PBLAP.fields_by_name['header'].message_type = _PBLAPHEADER
_PBLAP.fields_by_name['statistics'].message_type = _PBLAPSTATISTICS
_PBLAPSUMMARY.fields_by_name['best_lap_duration'].message_type = types_pb2._PBDURATION
_PBLAPSUMMARY.fields_by_name['average_lap_duration'].message_type = types_pb2._PBDURATION
_PBLAPS.fields_by_name['laps'].message_type = _PBLAP
_PBLAPS.fields_by_name['summary'].message_type = _PBLAPSUMMARY
_PBAUTOLAPS.fields_by_name['autoLaps'].message_type = _PBLAP
_PBAUTOLAPS.fields_by_name['summary'].message_type = _PBLAPSUMMARY
DESCRIPTOR.message_types_by_name['PbLapHeader'] = _PBLAPHEADER
DESCRIPTOR.message_types_by_name['PbLapSwimmingStatistics'] = _PBLAPSWIMMINGSTATISTICS
DESCRIPTOR.message_types_by_name['PbLapHeartRateStatistics'] = _PBLAPHEARTRATESTATISTICS
DESCRIPTOR.message_types_by_name['PbLapSpeedStatistics'] = _PBLAPSPEEDSTATISTICS
DESCRIPTOR.message_types_by_name['PbLapCadenceStatistics'] = _PBLAPCADENCESTATISTICS
DESCRIPTOR.message_types_by_name['PbLapPowerStatistics'] = _PBLAPPOWERSTATISTICS
DESCRIPTOR.message_types_by_name['PbLapLRBalanceStatistics'] = _PBLAPLRBALANCESTATISTICS
DESCRIPTOR.message_types_by_name['PbLapPedalingIndexStatistics'] = _PBLAPPEDALINGINDEXSTATISTICS
DESCRIPTOR.message_types_by_name['PbLapPedalingEfficiencyStatistics'] = _PBLAPPEDALINGEFFICIENCYSTATISTICS
DESCRIPTOR.message_types_by_name['PbLapInclineStatistics'] = _PBLAPINCLINESTATISTICS
DESCRIPTOR.message_types_by_name['PbLapStrideLengthStatistics'] = _PBLAPSTRIDELENGTHSTATISTICS
DESCRIPTOR.message_types_by_name['PbLapStatistics'] = _PBLAPSTATISTICS
DESCRIPTOR.message_types_by_name['PbLap'] = _PBLAP
DESCRIPTOR.message_types_by_name['PbLapSummary'] = _PBLAPSUMMARY
DESCRIPTOR.message_types_by_name['PbLaps'] = _PBLAPS
DESCRIPTOR.message_types_by_name['PbAutoLaps'] = _PBAUTOLAPS

PbLapHeader = _reflection.GeneratedProtocolMessageType('PbLapHeader', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPHEADER,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapHeader)
  ))
_sym_db.RegisterMessage(PbLapHeader)

PbLapSwimmingStatistics = _reflection.GeneratedProtocolMessageType('PbLapSwimmingStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPSWIMMINGSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapSwimmingStatistics)
  ))
_sym_db.RegisterMessage(PbLapSwimmingStatistics)

PbLapHeartRateStatistics = _reflection.GeneratedProtocolMessageType('PbLapHeartRateStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPHEARTRATESTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapHeartRateStatistics)
  ))
_sym_db.RegisterMessage(PbLapHeartRateStatistics)

PbLapSpeedStatistics = _reflection.GeneratedProtocolMessageType('PbLapSpeedStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPSPEEDSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapSpeedStatistics)
  ))
_sym_db.RegisterMessage(PbLapSpeedStatistics)

PbLapCadenceStatistics = _reflection.GeneratedProtocolMessageType('PbLapCadenceStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPCADENCESTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapCadenceStatistics)
  ))
_sym_db.RegisterMessage(PbLapCadenceStatistics)

PbLapPowerStatistics = _reflection.GeneratedProtocolMessageType('PbLapPowerStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPPOWERSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapPowerStatistics)
  ))
_sym_db.RegisterMessage(PbLapPowerStatistics)

PbLapLRBalanceStatistics = _reflection.GeneratedProtocolMessageType('PbLapLRBalanceStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPLRBALANCESTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapLRBalanceStatistics)
  ))
_sym_db.RegisterMessage(PbLapLRBalanceStatistics)

PbLapPedalingIndexStatistics = _reflection.GeneratedProtocolMessageType('PbLapPedalingIndexStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPPEDALINGINDEXSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapPedalingIndexStatistics)
  ))
_sym_db.RegisterMessage(PbLapPedalingIndexStatistics)

PbLapPedalingEfficiencyStatistics = _reflection.GeneratedProtocolMessageType('PbLapPedalingEfficiencyStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPPEDALINGEFFICIENCYSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapPedalingEfficiencyStatistics)
  ))
_sym_db.RegisterMessage(PbLapPedalingEfficiencyStatistics)

PbLapInclineStatistics = _reflection.GeneratedProtocolMessageType('PbLapInclineStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPINCLINESTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapInclineStatistics)
  ))
_sym_db.RegisterMessage(PbLapInclineStatistics)

PbLapStrideLengthStatistics = _reflection.GeneratedProtocolMessageType('PbLapStrideLengthStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPSTRIDELENGTHSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapStrideLengthStatistics)
  ))
_sym_db.RegisterMessage(PbLapStrideLengthStatistics)

PbLapStatistics = _reflection.GeneratedProtocolMessageType('PbLapStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPSTATISTICS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapStatistics)
  ))
_sym_db.RegisterMessage(PbLapStatistics)

PbLap = _reflection.GeneratedProtocolMessageType('PbLap', (_message.Message,), dict(
  DESCRIPTOR = _PBLAP,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLap)
  ))
_sym_db.RegisterMessage(PbLap)

PbLapSummary = _reflection.GeneratedProtocolMessageType('PbLapSummary', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPSUMMARY,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLapSummary)
  ))
_sym_db.RegisterMessage(PbLapSummary)

PbLaps = _reflection.GeneratedProtocolMessageType('PbLaps', (_message.Message,), dict(
  DESCRIPTOR = _PBLAPS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLaps)
  ))
_sym_db.RegisterMessage(PbLaps)

PbAutoLaps = _reflection.GeneratedProtocolMessageType('PbAutoLaps', (_message.Message,), dict(
  DESCRIPTOR = _PBAUTOLAPS,
  __module__ = 'exercise_laps_pb2'
  # @@protoc_insertion_point(class_scope:data.PbAutoLaps)
  ))
_sym_db.RegisterMessage(PbAutoLaps)


# @@protoc_insertion_point(module_scope)
