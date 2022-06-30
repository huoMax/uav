# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntask.proto\"L\n\x16\x46\x61\x63\x65RecognitionRequest\x12\x10\n\x08sequence\x18\x01 \x01(\x05\x12\x10\n\x08img_orig\x18\x02 \x01(\x0c\x12\x0e\n\x06target\x18\x03 \x01(\t\"\x95\x01\n\x15\x46\x61\x63\x65RecognitionReplay\x12\x10\n\x08sequence\x18\x01 \x01(\x05\x12\x0f\n\x07img_out\x18\x02 \x01(\x0c\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x14\n\x0c\x61rrival_time\x18\x04 \x01(\t\x12\x19\n\x11start_handle_time\x18\x05 \x01(\t\x12\x17\n\x0f\x65nd_handle_time\x18\x06 \x01(\t\"\x12\n\x10HeartbeatRequest\"\x11\n\x0fHeartbeatReplay2\xbc\x01\n\x0bTaskService\x12J\n\x15task_face_recognition\x12\x17.FaceRecognitionRequest\x1a\x16.FaceRecognitionReplay\"\x00\x12\x32\n\theartbeat\x12\x11.HeartbeatRequest\x1a\x10.HeartbeatReplay\"\x00\x12-\n\x04test\x12\x11.HeartbeatRequest\x1a\x10.HeartbeatReplay\"\x00\x62\x06proto3')



_FACERECOGNITIONREQUEST = DESCRIPTOR.message_types_by_name['FaceRecognitionRequest']
_FACERECOGNITIONREPLAY = DESCRIPTOR.message_types_by_name['FaceRecognitionReplay']
_HEARTBEATREQUEST = DESCRIPTOR.message_types_by_name['HeartbeatRequest']
_HEARTBEATREPLAY = DESCRIPTOR.message_types_by_name['HeartbeatReplay']
FaceRecognitionRequest = _reflection.GeneratedProtocolMessageType('FaceRecognitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _FACERECOGNITIONREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:FaceRecognitionRequest)
  })
_sym_db.RegisterMessage(FaceRecognitionRequest)

FaceRecognitionReplay = _reflection.GeneratedProtocolMessageType('FaceRecognitionReplay', (_message.Message,), {
  'DESCRIPTOR' : _FACERECOGNITIONREPLAY,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:FaceRecognitionReplay)
  })
_sym_db.RegisterMessage(FaceRecognitionReplay)

HeartbeatRequest = _reflection.GeneratedProtocolMessageType('HeartbeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:HeartbeatRequest)
  })
_sym_db.RegisterMessage(HeartbeatRequest)

HeartbeatReplay = _reflection.GeneratedProtocolMessageType('HeartbeatReplay', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREPLAY,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:HeartbeatReplay)
  })
_sym_db.RegisterMessage(HeartbeatReplay)

_TASKSERVICE = DESCRIPTOR.services_by_name['TaskService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FACERECOGNITIONREQUEST._serialized_start=14
  _FACERECOGNITIONREQUEST._serialized_end=90
  _FACERECOGNITIONREPLAY._serialized_start=93
  _FACERECOGNITIONREPLAY._serialized_end=242
  _HEARTBEATREQUEST._serialized_start=244
  _HEARTBEATREQUEST._serialized_end=262
  _HEARTBEATREPLAY._serialized_start=264
  _HEARTBEATREPLAY._serialized_end=281
  _TASKSERVICE._serialized_start=284
  _TASKSERVICE._serialized_end=472
# @@protoc_insertion_point(module_scope)
