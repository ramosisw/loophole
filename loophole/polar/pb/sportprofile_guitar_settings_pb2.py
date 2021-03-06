# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sportprofile_guitar_settings.proto

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
  name='sportprofile_guitar_settings.proto',
  package='data',
  serialized_pb=_b('\n\"sportprofile_guitar_settings.proto\x12\x04\x64\x61ta\x1a\x10structures.proto\x1a\x0btypes.proto\"\x94\x08\n\x1cPbGuitarSportProfileSettings\x12\x44\n\x0bheart_touch\x18\x01 \x01(\x0e\x32/.data.PbGuitarSportProfileSettings.PbHeartTouch\x12O\n\x11tap_button_action\x18\x02 \x01(\x0e\x32\x34.data.PbGuitarSportProfileSettings.PbTapButtonAction\x12\x11\n\tvibration\x18\x03 \x01(\x08\x12\x12\n\nauto_start\x18\x04 \x01(\x08\x12\x16\n\x0e\x61uto_scrolling\x18\x05 \x01(\x08\x12\x42\n\x1cstride_sensor_calib_settings\x18\x06 \x01(\x0b\x32\x1c.PbStrideSensorCalibSettings\x12!\n\x19sprint_display_activation\x18\x07 \x01(\r\x12\x89\x01\n\x1csport_tap_button_sensitivity\x18\x08 \x01(\x0e\x32>.data.PbGuitarSportProfileSettings.PbSportTapButtonSensitivity:#SPORT_TAP_BUTTON_SENSITIVITY_MEDIUM\x12*\n\rswimming_pool\x18\t \x01(\x0b\x32\x13.PbSwimmingPoolInfo\"\x8c\x01\n\x0cPbHeartTouch\x12\x13\n\x0fHEART_TOUCH_OFF\x10\x01\x12\"\n\x1eHEART_TOUCH_ACTIVATE_BACKLIGHT\x10\x02\x12!\n\x1dHEART_TOUCH_SHOW_PREVIOUS_LAP\x10\x03\x12 \n\x1cHEART_TOUCH_SHOW_TIME_OF_DAY\x10\x04\"\x88\x01\n\x11PbTapButtonAction\x12\x12\n\x0eTAP_BUTTON_OFF\x10\x01\x12\x17\n\x13TAP_BUTTON_TAKE_LAP\x10\x02\x12#\n\x1fTAP_BUTTON_CHANGE_TRAINING_VIEW\x10\x03\x12!\n\x1dTAP_BUTTON_ACTIVATE_BACKLIGHT\x10\x04\"\xe4\x01\n\x1bPbSportTapButtonSensitivity\x12$\n SPORT_TAP_BUTTON_SENSITIVITY_OFF\x10\x01\x12)\n%SPORT_TAP_BUTTON_SENSITIVITY_VERY_LOW\x10\x05\x12$\n SPORT_TAP_BUTTON_SENSITIVITY_LOW\x10\x02\x12\'\n#SPORT_TAP_BUTTON_SENSITIVITY_MEDIUM\x10\x03\x12%\n!SPORT_TAP_BUTTON_SENSITIVITY_HIGH\x10\x04')
  ,
  dependencies=[structures_pb2.DESCRIPTOR,types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PBGUITARSPORTPROFILESETTINGS_PBHEARTTOUCH = _descriptor.EnumDescriptor(
  name='PbHeartTouch',
  full_name='data.PbGuitarSportProfileSettings.PbHeartTouch',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_OFF', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_ACTIVATE_BACKLIGHT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_SHOW_PREVIOUS_LAP', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_SHOW_TIME_OF_DAY', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=610,
  serialized_end=750,
)
_sym_db.RegisterEnumDescriptor(_PBGUITARSPORTPROFILESETTINGS_PBHEARTTOUCH)

_PBGUITARSPORTPROFILESETTINGS_PBTAPBUTTONACTION = _descriptor.EnumDescriptor(
  name='PbTapButtonAction',
  full_name='data.PbGuitarSportProfileSettings.PbTapButtonAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TAP_BUTTON_OFF', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAP_BUTTON_TAKE_LAP', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAP_BUTTON_CHANGE_TRAINING_VIEW', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAP_BUTTON_ACTIVATE_BACKLIGHT', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=753,
  serialized_end=889,
)
_sym_db.RegisterEnumDescriptor(_PBGUITARSPORTPROFILESETTINGS_PBTAPBUTTONACTION)

_PBGUITARSPORTPROFILESETTINGS_PBSPORTTAPBUTTONSENSITIVITY = _descriptor.EnumDescriptor(
  name='PbSportTapButtonSensitivity',
  full_name='data.PbGuitarSportProfileSettings.PbSportTapButtonSensitivity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPORT_TAP_BUTTON_SENSITIVITY_OFF', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TAP_BUTTON_SENSITIVITY_VERY_LOW', index=1, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TAP_BUTTON_SENSITIVITY_LOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TAP_BUTTON_SENSITIVITY_MEDIUM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TAP_BUTTON_SENSITIVITY_HIGH', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=892,
  serialized_end=1120,
)
_sym_db.RegisterEnumDescriptor(_PBGUITARSPORTPROFILESETTINGS_PBSPORTTAPBUTTONSENSITIVITY)


_PBGUITARSPORTPROFILESETTINGS = _descriptor.Descriptor(
  name='PbGuitarSportProfileSettings',
  full_name='data.PbGuitarSportProfileSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heart_touch', full_name='data.PbGuitarSportProfileSettings.heart_touch', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tap_button_action', full_name='data.PbGuitarSportProfileSettings.tap_button_action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vibration', full_name='data.PbGuitarSportProfileSettings.vibration', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_start', full_name='data.PbGuitarSportProfileSettings.auto_start', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_scrolling', full_name='data.PbGuitarSportProfileSettings.auto_scrolling', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride_sensor_calib_settings', full_name='data.PbGuitarSportProfileSettings.stride_sensor_calib_settings', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sprint_display_activation', full_name='data.PbGuitarSportProfileSettings.sprint_display_activation', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sport_tap_button_sensitivity', full_name='data.PbGuitarSportProfileSettings.sport_tap_button_sensitivity', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swimming_pool', full_name='data.PbGuitarSportProfileSettings.swimming_pool', index=8,
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
    _PBGUITARSPORTPROFILESETTINGS_PBHEARTTOUCH,
    _PBGUITARSPORTPROFILESETTINGS_PBTAPBUTTONACTION,
    _PBGUITARSPORTPROFILESETTINGS_PBSPORTTAPBUTTONSENSITIVITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=1120,
)

_PBGUITARSPORTPROFILESETTINGS.fields_by_name['heart_touch'].enum_type = _PBGUITARSPORTPROFILESETTINGS_PBHEARTTOUCH
_PBGUITARSPORTPROFILESETTINGS.fields_by_name['tap_button_action'].enum_type = _PBGUITARSPORTPROFILESETTINGS_PBTAPBUTTONACTION
_PBGUITARSPORTPROFILESETTINGS.fields_by_name['stride_sensor_calib_settings'].message_type = types_pb2._PBSTRIDESENSORCALIBSETTINGS
_PBGUITARSPORTPROFILESETTINGS.fields_by_name['sport_tap_button_sensitivity'].enum_type = _PBGUITARSPORTPROFILESETTINGS_PBSPORTTAPBUTTONSENSITIVITY
_PBGUITARSPORTPROFILESETTINGS.fields_by_name['swimming_pool'].message_type = structures_pb2._PBSWIMMINGPOOLINFO
_PBGUITARSPORTPROFILESETTINGS_PBHEARTTOUCH.containing_type = _PBGUITARSPORTPROFILESETTINGS
_PBGUITARSPORTPROFILESETTINGS_PBTAPBUTTONACTION.containing_type = _PBGUITARSPORTPROFILESETTINGS
_PBGUITARSPORTPROFILESETTINGS_PBSPORTTAPBUTTONSENSITIVITY.containing_type = _PBGUITARSPORTPROFILESETTINGS
DESCRIPTOR.message_types_by_name['PbGuitarSportProfileSettings'] = _PBGUITARSPORTPROFILESETTINGS

PbGuitarSportProfileSettings = _reflection.GeneratedProtocolMessageType('PbGuitarSportProfileSettings', (_message.Message,), dict(
  DESCRIPTOR = _PBGUITARSPORTPROFILESETTINGS,
  __module__ = 'sportprofile_guitar_settings_pb2'
  # @@protoc_insertion_point(class_scope:data.PbGuitarSportProfileSettings)
  ))
_sym_db.RegisterMessage(PbGuitarSportProfileSettings)


# @@protoc_insertion_point(module_scope)
