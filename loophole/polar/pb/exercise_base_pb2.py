# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exercise_base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import structures_pb2
import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exercise_base.proto',
  package='data',
  serialized_pb=_b('\n\x13\x65xercise_base.proto\x12\x04\x64\x61ta\x1a\x10structures.proto\x1a\x0btypes.proto\"*\n\x12PbExerciseCounters\x12\x14\n\x0csprint_count\x18\x01 \x01(\r\"\x8a\x04\n\x0ePbExerciseBase\x12\x1f\n\x05start\x18\x01 \x02(\x0b\x32\x10.PbLocalDateTime\x12\x1d\n\x08\x64uration\x18\x02 \x02(\x0b\x32\x0b.PbDuration\x12!\n\x05sport\x18\x03 \x02(\x0b\x32\x12.PbSportIdentifier\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\x12\x10\n\x08\x63\x61lories\x18\x05 \x01(\r\x12&\n\rtraining_load\x18\x06 \x01(\x0b\x32\x0f.PbTrainingLoad\x12\x31\n\x19\x61vailable_sensor_features\x18\x07 \x03(\x0e\x32\x0e.PbFeatureType\x12&\n\rrunning_index\x18\t \x01(\x0b\x32\x0f.PbRunningIndex\x12\x0e\n\x06\x61scent\x18\n \x01(\x02\x12\x0f\n\x07\x64\x65scent\x18\x0b \x01(\x02\x12\x10\n\x08latitude\x18\x0c \x01(\x01\x12\x11\n\tlongitude\x18\r \x01(\x01\x12\r\n\x05place\x18\x0e \x01(\t\x12\x33\n\x11\x65xercise_counters\x18\x10 \x01(\x0b\x32\x18.data.PbExerciseCounters\x12#\n\x18speed_calibration_offset\x18\x11 \x01(\x02:\x01\x30\x12\x18\n\x10walking_distance\x18\x12 \x01(\x02\x12%\n\x10walking_duration\x18\x13 \x01(\x0b\x32\x0b.PbDuration')
  ,
  dependencies=[structures_pb2.DESCRIPTOR,types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBEXERCISECOUNTERS = _descriptor.Descriptor(
  name='PbExerciseCounters',
  full_name='data.PbExerciseCounters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sprint_count', full_name='data.PbExerciseCounters.sprint_count', index=0,
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
  serialized_start=60,
  serialized_end=102,
)


_PBEXERCISEBASE = _descriptor.Descriptor(
  name='PbExerciseBase',
  full_name='data.PbExerciseBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='data.PbExerciseBase.start', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='data.PbExerciseBase.duration', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sport', full_name='data.PbExerciseBase.sport', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='data.PbExerciseBase.distance', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calories', full_name='data.PbExerciseBase.calories', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='training_load', full_name='data.PbExerciseBase.training_load', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='available_sensor_features', full_name='data.PbExerciseBase.available_sensor_features', index=6,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='running_index', full_name='data.PbExerciseBase.running_index', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ascent', full_name='data.PbExerciseBase.ascent', index=8,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='descent', full_name='data.PbExerciseBase.descent', index=9,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='data.PbExerciseBase.latitude', index=10,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='data.PbExerciseBase.longitude', index=11,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place', full_name='data.PbExerciseBase.place', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exercise_counters', full_name='data.PbExerciseBase.exercise_counters', index=13,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_calibration_offset', full_name='data.PbExerciseBase.speed_calibration_offset', index=14,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='walking_distance', full_name='data.PbExerciseBase.walking_distance', index=15,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='walking_duration', full_name='data.PbExerciseBase.walking_duration', index=16,
      number=19, type=11, cpp_type=10, label=1,
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
  serialized_start=105,
  serialized_end=627,
)

_PBEXERCISEBASE.fields_by_name['start'].message_type = types_pb2._PBLOCALDATETIME
_PBEXERCISEBASE.fields_by_name['duration'].message_type = types_pb2._PBDURATION
_PBEXERCISEBASE.fields_by_name['sport'].message_type = structures_pb2._PBSPORTIDENTIFIER
_PBEXERCISEBASE.fields_by_name['training_load'].message_type = structures_pb2._PBTRAININGLOAD
_PBEXERCISEBASE.fields_by_name['available_sensor_features'].enum_type = types_pb2._PBFEATURETYPE
_PBEXERCISEBASE.fields_by_name['running_index'].message_type = structures_pb2._PBRUNNINGINDEX
_PBEXERCISEBASE.fields_by_name['exercise_counters'].message_type = _PBEXERCISECOUNTERS
_PBEXERCISEBASE.fields_by_name['walking_duration'].message_type = types_pb2._PBDURATION
DESCRIPTOR.message_types_by_name['PbExerciseCounters'] = _PBEXERCISECOUNTERS
DESCRIPTOR.message_types_by_name['PbExerciseBase'] = _PBEXERCISEBASE

PbExerciseCounters = _reflection.GeneratedProtocolMessageType('PbExerciseCounters', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISECOUNTERS,
  __module__ = 'exercise_base_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseCounters)
  ))
_sym_db.RegisterMessage(PbExerciseCounters)

PbExerciseBase = _reflection.GeneratedProtocolMessageType('PbExerciseBase', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISEBASE,
  __module__ = 'exercise_base_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseBase)
  ))
_sym_db.RegisterMessage(PbExerciseBase)


# @@protoc_insertion_point(module_scope)
