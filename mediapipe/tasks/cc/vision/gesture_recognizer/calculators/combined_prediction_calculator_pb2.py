# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/gesture_recognizer/calculators/combined_prediction_calculator.proto
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
  name='mediapipe/tasks/cc/vision/gesture_recognizer/calculators/combined_prediction_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n]mediapipe/tasks/cc/vision/gesture_recognizer/calculators/combined_prediction_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xb9\x02\n#CombinedPredictionCalculatorOptions\x12\x43\n\x05\x63lass\x18\x01 \x03(\x0b\x32\x34.mediapipe.CombinedPredictionCalculatorOptions.Class\x12#\n\x18\x64\x65\x66\x61ult_global_threshold\x18\x02 \x01(\x02:\x01\x30\x12\x18\n\x10\x62\x61\x63kground_label\x18\x03 \x01(\t\x1a/\n\x05\x43lass\x12\r\n\x05label\x18\x01 \x01(\t\x12\x17\n\x0fscore_threshold\x18\x02 \x01(\x02\x32]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8b\x88\xd5\xe6\x01 \x01(\x0b\x32..mediapipe.CombinedPredictionCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_COMBINEDPREDICTIONCALCULATOROPTIONS_CLASS = _descriptor.Descriptor(
  name='Class',
  full_name='mediapipe.CombinedPredictionCalculatorOptions.Class',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='mediapipe.CombinedPredictionCalculatorOptions.Class.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score_threshold', full_name='mediapipe.CombinedPredictionCalculatorOptions.Class.score_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
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
  serialized_start=318,
  serialized_end=365,
)

_COMBINEDPREDICTIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='CombinedPredictionCalculatorOptions',
  full_name='mediapipe.CombinedPredictionCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class', full_name='mediapipe.CombinedPredictionCalculatorOptions.class', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_global_threshold', full_name='mediapipe.CombinedPredictionCalculatorOptions.default_global_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='background_label', full_name='mediapipe.CombinedPredictionCalculatorOptions.background_label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.CombinedPredictionCalculatorOptions.ext', index=0,
      number=483738635, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[_COMBINEDPREDICTIONCALCULATOROPTIONS_CLASS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=460,
)

_COMBINEDPREDICTIONCALCULATOROPTIONS_CLASS.containing_type = _COMBINEDPREDICTIONCALCULATOROPTIONS
_COMBINEDPREDICTIONCALCULATOROPTIONS.fields_by_name['class'].message_type = _COMBINEDPREDICTIONCALCULATOROPTIONS_CLASS
DESCRIPTOR.message_types_by_name['CombinedPredictionCalculatorOptions'] = _COMBINEDPREDICTIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombinedPredictionCalculatorOptions = _reflection.GeneratedProtocolMessageType('CombinedPredictionCalculatorOptions', (_message.Message,), {

  'Class' : _reflection.GeneratedProtocolMessageType('Class', (_message.Message,), {
    'DESCRIPTOR' : _COMBINEDPREDICTIONCALCULATOROPTIONS_CLASS,
    '__module__' : 'mediapipe.tasks.cc.vision.gesture_recognizer.calculators.combined_prediction_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.CombinedPredictionCalculatorOptions.Class)
    })
  ,
  'DESCRIPTOR' : _COMBINEDPREDICTIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.tasks.cc.vision.gesture_recognizer.calculators.combined_prediction_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.CombinedPredictionCalculatorOptions)
  })
_sym_db.RegisterMessage(CombinedPredictionCalculatorOptions)
_sym_db.RegisterMessage(CombinedPredictionCalculatorOptions.Class)

_COMBINEDPREDICTIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _COMBINEDPREDICTIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_COMBINEDPREDICTIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
