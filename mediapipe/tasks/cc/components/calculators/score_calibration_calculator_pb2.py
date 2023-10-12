# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/calculators/score_calibration_calculator.proto
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
  name='mediapipe/tasks/cc/components/calculators/score_calibration_calculator.proto',
  package='mediapipe.tasks',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nLmediapipe/tasks/cc/components/calculators/score_calibration_calculator.proto\x12\x0fmediapipe.tasks\x1a$mediapipe/framework/calculator.proto\"\xfc\x03\n!ScoreCalibrationCalculatorOptions\x12L\n\x08sigmoids\x18\x01 \x03(\x0b\x32:.mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid\x12n\n\x14score_transformation\x18\x02 \x01(\x0e\x32\x46.mediapipe.tasks.ScoreCalibrationCalculatorOptions.ScoreTransformation:\x08IDENTITY\x12\x15\n\rdefault_score\x18\x03 \x01(\x02\x1aJ\n\x07Sigmoid\x12\r\n\x05scale\x18\x01 \x01(\x02\x12\r\n\x05slope\x18\x02 \x01(\x02\x12\x0e\n\x06offset\x18\x03 \x01(\x02\x12\x11\n\tmin_score\x18\x04 \x01(\x02\"S\n\x13ScoreTransformation\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08IDENTITY\x10\x01\x12\x07\n\x03LOG\x10\x02\x12\x14\n\x10INVERSE_LOGISTIC\x10\x03\x32\x61\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x9e\xff\x9a\xe0\x01 \x01(\x0b\x32\x32.mediapipe.tasks.ScoreCalibrationCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])



_SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION = _descriptor.EnumDescriptor(
  name='ScoreTransformation',
  full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.ScoreTransformation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IDENTITY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVERSE_LOGISTIC', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=462,
  serialized_end=545,
)
_sym_db.RegisterEnumDescriptor(_SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION)


_SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID = _descriptor.Descriptor(
  name='Sigmoid',
  full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scale', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid.scale', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slope', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid.slope', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid.offset', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_score', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid.min_score', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=386,
  serialized_end=460,
)

_SCORECALIBRATIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ScoreCalibrationCalculatorOptions',
  full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sigmoids', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.sigmoids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score_transformation', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.score_transformation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_score', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.default_score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.ScoreCalibrationCalculatorOptions.ext', index=0,
      number=470204318, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[_SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID, ],
  enum_types=[
    _SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=644,
)

_SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID.containing_type = _SCORECALIBRATIONCALCULATOROPTIONS
_SCORECALIBRATIONCALCULATOROPTIONS.fields_by_name['sigmoids'].message_type = _SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID
_SCORECALIBRATIONCALCULATOROPTIONS.fields_by_name['score_transformation'].enum_type = _SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION
_SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION.containing_type = _SCORECALIBRATIONCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['ScoreCalibrationCalculatorOptions'] = _SCORECALIBRATIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScoreCalibrationCalculatorOptions = _reflection.GeneratedProtocolMessageType('ScoreCalibrationCalculatorOptions', (_message.Message,), {

  'Sigmoid' : _reflection.GeneratedProtocolMessageType('Sigmoid', (_message.Message,), {
    'DESCRIPTOR' : _SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID,
    '__module__' : 'mediapipe.tasks.cc.components.calculators.score_calibration_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid)
    })
  ,
  'DESCRIPTOR' : _SCORECALIBRATIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.tasks.cc.components.calculators.score_calibration_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.ScoreCalibrationCalculatorOptions)
  })
_sym_db.RegisterMessage(ScoreCalibrationCalculatorOptions)
_sym_db.RegisterMessage(ScoreCalibrationCalculatorOptions.Sigmoid)

_SCORECALIBRATIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SCORECALIBRATIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SCORECALIBRATIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
