# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cprotos.proto\"\xac\x01\n\x05\x44\x65pth\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\t\x12\r\n\x05quote\x18\x03 \x01(\t\x12\x1b\n\x04\x62ids\x18\x04 \x03(\x0b\x32\r.Depth.BidAsk\x12\x1b\n\x04\x61sks\x18\x05 \x03(\x0b\x32\r.Depth.BidAsk\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x1a\'\n\x06\x42idAsk\x12\r\n\x05price\x18\x01 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x62\x06proto3')
)




_DEPTH_BIDASK = _descriptor.Descriptor(
  name='BidAsk',
  full_name='Depth.BidAsk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='Depth.BidAsk.price', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Depth.BidAsk.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=189,
)

_DEPTH = _descriptor.Descriptor(
  name='Depth',
  full_name='Depth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange', full_name='Depth.exchange', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='Depth.base', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quote', full_name='Depth.quote', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bids', full_name='Depth.bids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asks', full_name='Depth.asks', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Depth.timestamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPTH_BIDASK, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=189,
)

_DEPTH_BIDASK.containing_type = _DEPTH
_DEPTH.fields_by_name['bids'].message_type = _DEPTH_BIDASK
_DEPTH.fields_by_name['asks'].message_type = _DEPTH_BIDASK
DESCRIPTOR.message_types_by_name['Depth'] = _DEPTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Depth = _reflection.GeneratedProtocolMessageType('Depth', (_message.Message,), dict(

  BidAsk = _reflection.GeneratedProtocolMessageType('BidAsk', (_message.Message,), dict(
    DESCRIPTOR = _DEPTH_BIDASK,
    __module__ = 'protos_pb2'
    # @@protoc_insertion_point(class_scope:Depth.BidAsk)
    ))
  ,
  DESCRIPTOR = _DEPTH,
  __module__ = 'protos_pb2'
  # @@protoc_insertion_point(class_scope:Depth)
  ))
_sym_db.RegisterMessage(Depth)
_sym_db.RegisterMessage(Depth.BidAsk)


# @@protoc_insertion_point(module_scope)
