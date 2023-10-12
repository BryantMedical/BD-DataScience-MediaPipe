# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/get_vector_item_calculator.proto
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
  name='mediapipe/calculators/core/get_vector_item_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;mediapipe/calculators/core/get_vector_item_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xab\x01\n\x1eGetVectorItemCalculatorOptions\x12\x12\n\nitem_index\x18\x01 \x01(\x05\x12\x1b\n\x13output_empty_on_oob\x18\x02 \x01(\x08\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xef\x92\x84\xdd\x01 \x01(\x0b\x32).mediapipe.GetVectorItemCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_GETVECTORITEMCALCULATOROPTIONS = _descriptor.Descriptor(
  name='GetVectorItemCalculatorOptions',
  full_name='mediapipe.GetVectorItemCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_index', full_name='mediapipe.GetVectorItemCalculatorOptions.item_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_empty_on_oob', full_name='mediapipe.GetVectorItemCalculatorOptions.output_empty_on_oob', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.GetVectorItemCalculatorOptions.ext', index=0,
      number=463538543, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=284,
)

DESCRIPTOR.message_types_by_name['GetVectorItemCalculatorOptions'] = _GETVECTORITEMCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVectorItemCalculatorOptions = _reflection.GeneratedProtocolMessageType('GetVectorItemCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _GETVECTORITEMCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.core.get_vector_item_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.GetVectorItemCalculatorOptions)
  })
_sym_db.RegisterMessage(GetVectorItemCalculatorOptions)

_GETVECTORITEMCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _GETVECTORITEMCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_GETVECTORITEMCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
