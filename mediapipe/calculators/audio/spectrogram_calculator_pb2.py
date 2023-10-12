# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/audio/spectrogram_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/audio/spectrogram_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8mediapipe/calculators/audio/spectrogram_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xfe\x04\n\x1cSpectrogramCalculatorOptions\x12\x1e\n\x16\x66rame_duration_seconds\x18\x01 \x01(\x01\x12 \n\x15\x66rame_overlap_seconds\x18\x02 \x01(\x01:\x01\x30\x12\x1e\n\x10pad_final_packet\x18\x03 \x01(\x08:\x04true\x12Z\n\x0boutput_type\x18\x04 \x01(\x0e\x32\x32.mediapipe.SpectrogramCalculatorOptions.OutputType:\x11SQUARED_MAGNITUDE\x12\'\n\x18\x61llow_multichannel_input\x18\x05 \x01(\x08:\x05\x66\x61lse\x12M\n\x0bwindow_type\x18\x06 \x01(\x0e\x32\x32.mediapipe.SpectrogramCalculatorOptions.WindowType:\x04HANN\x12\x17\n\x0coutput_scale\x18\x07 \x01(\x01:\x01\x31\x12\"\n\x13use_local_timestamp\x18\x08 \x01(\x08:\x05\x66\x61lse\"T\n\nOutputType\x12\x15\n\x11SQUARED_MAGNITUDE\x10\x00\x12\x14\n\x10LINEAR_MAGNITUDE\x10\x01\x12\x0c\n\x08\x44\x45\x43IBELS\x10\x02\x12\x0b\n\x07\x43OMPLEX\x10\x03\">\n\nWindowType\x12\x08\n\x04HANN\x10\x00\x12\x0b\n\x07HAMMING\x10\x01\x12\n\n\x06\x43OSINE\x10\x02\x12\r\n\tSQRT_HANN\x10\x04\x32U\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xc0\x88\xaa$ \x01(\x0b\x32\'.mediapipe.SpectrogramCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_SPECTROGRAMCALCULATOROPTIONS_OUTPUTTYPE = _descriptor.EnumDescriptor(
  name='OutputType',
  full_name='mediapipe.SpectrogramCalculatorOptions.OutputType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SQUARED_MAGNITUDE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINEAR_MAGNITUDE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DECIBELS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLEX', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=513,
  serialized_end=597,
)
_sym_db.RegisterEnumDescriptor(_SPECTROGRAMCALCULATOROPTIONS_OUTPUTTYPE)

_SPECTROGRAMCALCULATOROPTIONS_WINDOWTYPE = _descriptor.EnumDescriptor(
  name='WindowType',
  full_name='mediapipe.SpectrogramCalculatorOptions.WindowType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HANN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HAMMING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COSINE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SQRT_HANN', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=599,
  serialized_end=661,
)
_sym_db.RegisterEnumDescriptor(_SPECTROGRAMCALCULATOROPTIONS_WINDOWTYPE)


_SPECTROGRAMCALCULATOROPTIONS = _descriptor.Descriptor(
  name='SpectrogramCalculatorOptions',
  full_name='mediapipe.SpectrogramCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_duration_seconds', full_name='mediapipe.SpectrogramCalculatorOptions.frame_duration_seconds', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_overlap_seconds', full_name='mediapipe.SpectrogramCalculatorOptions.frame_overlap_seconds', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pad_final_packet', full_name='mediapipe.SpectrogramCalculatorOptions.pad_final_packet', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_type', full_name='mediapipe.SpectrogramCalculatorOptions.output_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_multichannel_input', full_name='mediapipe.SpectrogramCalculatorOptions.allow_multichannel_input', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='window_type', full_name='mediapipe.SpectrogramCalculatorOptions.window_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_scale', full_name='mediapipe.SpectrogramCalculatorOptions.output_scale', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_local_timestamp', full_name='mediapipe.SpectrogramCalculatorOptions.use_local_timestamp', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.SpectrogramCalculatorOptions.ext', index=0,
      number=76186688, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
    _SPECTROGRAMCALCULATOROPTIONS_OUTPUTTYPE,
    _SPECTROGRAMCALCULATOROPTIONS_WINDOWTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=748,
)

_SPECTROGRAMCALCULATOROPTIONS.fields_by_name['output_type'].enum_type = _SPECTROGRAMCALCULATOROPTIONS_OUTPUTTYPE
_SPECTROGRAMCALCULATOROPTIONS.fields_by_name['window_type'].enum_type = _SPECTROGRAMCALCULATOROPTIONS_WINDOWTYPE
_SPECTROGRAMCALCULATOROPTIONS_OUTPUTTYPE.containing_type = _SPECTROGRAMCALCULATOROPTIONS
_SPECTROGRAMCALCULATOROPTIONS_WINDOWTYPE.containing_type = _SPECTROGRAMCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['SpectrogramCalculatorOptions'] = _SPECTROGRAMCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpectrogramCalculatorOptions = _reflection.GeneratedProtocolMessageType('SpectrogramCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _SPECTROGRAMCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.audio.spectrogram_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SpectrogramCalculatorOptions)
  })
_sym_db.RegisterMessage(SpectrogramCalculatorOptions)

_SPECTROGRAMCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SPECTROGRAMCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SPECTROGRAMCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
