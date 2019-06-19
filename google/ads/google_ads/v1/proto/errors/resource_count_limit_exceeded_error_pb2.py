# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/resource_count_limit_exceeded_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/errors/resource_count_limit_exceeded_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB$ResourceCountLimitExceededErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\nNgoogle/ads/googleads_v1/proto/errors/resource_count_limit_exceeded_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\xaa\x02\n#ResourceCountLimitExceededErrorEnum\"\x82\x02\n\x1fResourceCountLimitExceededError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rACCOUNT_LIMIT\x10\x02\x12\x12\n\x0e\x43\x41MPAIGN_LIMIT\x10\x03\x12\x11\n\rADGROUP_LIMIT\x10\x04\x12\x15\n\x11\x41\x44_GROUP_AD_LIMIT\x10\x05\x12\x1c\n\x18\x41\x44_GROUP_CRITERION_LIMIT\x10\x06\x12\x14\n\x10SHARED_SET_LIMIT\x10\x07\x12\x1b\n\x17MATCHING_FUNCTION_LIMIT\x10\x08\x12\x1f\n\x1bRESPONSE_ROW_LIMIT_EXCEEDED\x10\tB\xff\x01\n\"com.google.ads.googleads.v1.errorsB$ResourceCountLimitExceededErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_RESOURCECOUNTLIMITEXCEEDEDERRORENUM_RESOURCECOUNTLIMITEXCEEDEDERROR = _descriptor.EnumDescriptor(
  name='ResourceCountLimitExceededError',
  full_name='google.ads.googleads.v1.errors.ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_LIMIT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_LIMIT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADGROUP_LIMIT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_AD_LIMIT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_CRITERION_LIMIT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARED_SET_LIMIT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATCHING_FUNCTION_LIMIT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_ROW_LIMIT_EXCEEDED', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=185,
  serialized_end=443,
)
_sym_db.RegisterEnumDescriptor(_RESOURCECOUNTLIMITEXCEEDEDERRORENUM_RESOURCECOUNTLIMITEXCEEDEDERROR)


_RESOURCECOUNTLIMITEXCEEDEDERRORENUM = _descriptor.Descriptor(
  name='ResourceCountLimitExceededErrorEnum',
  full_name='google.ads.googleads.v1.errors.ResourceCountLimitExceededErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESOURCECOUNTLIMITEXCEEDEDERRORENUM_RESOURCECOUNTLIMITEXCEEDEDERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=443,
)

_RESOURCECOUNTLIMITEXCEEDEDERRORENUM_RESOURCECOUNTLIMITEXCEEDEDERROR.containing_type = _RESOURCECOUNTLIMITEXCEEDEDERRORENUM
DESCRIPTOR.message_types_by_name['ResourceCountLimitExceededErrorEnum'] = _RESOURCECOUNTLIMITEXCEEDEDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceCountLimitExceededErrorEnum = _reflection.GeneratedProtocolMessageType('ResourceCountLimitExceededErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCECOUNTLIMITEXCEEDEDERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.resource_count_limit_exceeded_error_pb2'
  ,
  __doc__ = """Container for enum describing possible resource count limit exceeded
  errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.ResourceCountLimitExceededErrorEnum)
  ))
_sym_db.RegisterMessage(ResourceCountLimitExceededErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)