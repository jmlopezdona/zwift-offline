# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: playback.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eplayback.proto\"@\n\x08Playback\x12\x12\n\nsegment_id\x18\x01 \x02(\x04\x12\x0c\n\x04time\x18\x03 \x02(\x02\x12\x12\n\nworld_time\x18\x04 \x02(\x04\"c\n\x10PlaybackResponse\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x12\n\nsegment_id\x18\x02 \x02(\x04\x12\x0c\n\x04time\x18\x04 \x02(\x02\x12\x12\n\nworld_time\x18\x05 \x02(\x04\x12\x0b\n\x03url\x18\x06 \x02(\t')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'playback_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYBACK._serialized_start=18
  _PLAYBACK._serialized_end=82
  _PLAYBACKRESPONSE._serialized_start=84
  _PLAYBACKRESPONSE._serialized_end=183
# @@protoc_insertion_point(module_scope)
