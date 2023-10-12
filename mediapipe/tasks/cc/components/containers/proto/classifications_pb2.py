# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/containers/proto/classifications.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework.formats import classification_pb2 as mediapipe_dot_framework_dot_formats_dot_classification__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/components/containers/proto/classifications.proto',
  package='mediapipe.tasks.components.containers.proto',
  syntax='proto2',
  serialized_options=b'\n6com.google.mediapipe.tasks.components.containers.protoB\024ClassificationsProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDmediapipe/tasks/cc/components/containers/proto/classifications.proto\x12+mediapipe.tasks.components.containers.proto\x1a\x30mediapipe/framework/formats/classification.proto\"z\n\x0f\x43lassifications\x12:\n\x13\x63lassification_list\x18\x04 \x01(\x0b\x32\x1d.mediapipe.ClassificationList\x12\x12\n\nhead_index\x18\x02 \x01(\x05\x12\x11\n\thead_name\x18\x03 \x01(\tJ\x04\x08\x01\x10\x02\"\x83\x01\n\x14\x43lassificationResult\x12U\n\x0f\x63lassifications\x18\x01 \x03(\x0b\x32<.mediapipe.tasks.components.containers.proto.Classifications\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\x42N\n6com.google.mediapipe.tasks.components.containers.protoB\x14\x43lassificationsProto'
  ,
  dependencies=[mediapipe_dot_framework_dot_formats_dot_classification__pb2.DESCRIPTOR,])




_CLASSIFICATIONS = _descriptor.Descriptor(
  name='Classifications',
  full_name='mediapipe.tasks.components.containers.proto.Classifications',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification_list', full_name='mediapipe.tasks.components.containers.proto.Classifications.classification_list', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head_index', full_name='mediapipe.tasks.components.containers.proto.Classifications.head_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head_name', full_name='mediapipe.tasks.components.containers.proto.Classifications.head_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=167,
  serialized_end=289,
)


_CLASSIFICATIONRESULT = _descriptor.Descriptor(
  name='ClassificationResult',
  full_name='mediapipe.tasks.components.containers.proto.ClassificationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classifications', full_name='mediapipe.tasks.components.containers.proto.ClassificationResult.classifications', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='mediapipe.tasks.components.containers.proto.ClassificationResult.timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=292,
  serialized_end=423,
)

_CLASSIFICATIONS.fields_by_name['classification_list'].message_type = mediapipe_dot_framework_dot_formats_dot_classification__pb2._CLASSIFICATIONLIST
_CLASSIFICATIONRESULT.fields_by_name['classifications'].message_type = _CLASSIFICATIONS
DESCRIPTOR.message_types_by_name['Classifications'] = _CLASSIFICATIONS
DESCRIPTOR.message_types_by_name['ClassificationResult'] = _CLASSIFICATIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Classifications = _reflection.GeneratedProtocolMessageType('Classifications', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONS,
  '__module__' : 'mediapipe.tasks.cc.components.containers.proto.classifications_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.components.containers.proto.Classifications)
  })
_sym_db.RegisterMessage(Classifications)

ClassificationResult = _reflection.GeneratedProtocolMessageType('ClassificationResult', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONRESULT,
  '__module__' : 'mediapipe.tasks.cc.components.containers.proto.classifications_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.components.containers.proto.ClassificationResult)
  })
_sym_db.RegisterMessage(ClassificationResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
