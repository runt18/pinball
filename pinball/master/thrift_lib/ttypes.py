#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ErrorCode:
  UNKNOWN = 0
  VERSION_CONFLICT = 1
  NOT_FOUND = 2
  INPUT_ERROR = 3

  _VALUES_TO_NAMES = {
    0: "UNKNOWN",
    1: "VERSION_CONFLICT",
    2: "NOT_FOUND",
    3: "INPUT_ERROR",
  }

  _NAMES_TO_VALUES = {
    "UNKNOWN": 0,
    "VERSION_CONFLICT": 1,
    "NOT_FOUND": 2,
    "INPUT_ERROR": 3,
  }


class Token:
  """
  Attributes:
   - version
   - name
   - owner
   - expirationTime
   - priority
   - data
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'version', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'owner', None, None, ), # 3
    (4, TType.I64, 'expirationTime', None, None, ), # 4
    (5, TType.DOUBLE, 'priority', None, 0, ), # 5
    (6, TType.STRING, 'data', None, None, ), # 6
  )

  def __init__(self, version=None, name=None, owner=None, expirationTime=None, priority=thrift_spec[5][4], data=None,):
    self.version = version
    self.name = name
    self.owner = owner
    self.expirationTime = expirationTime
    self.priority = priority
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.version = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.owner = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.expirationTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.DOUBLE:
          self.priority = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.data = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Token')
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.I64, 1)
      oprot.writeI64(self.version)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.owner is not None:
      oprot.writeFieldBegin('owner', TType.STRING, 3)
      oprot.writeString(self.owner)
      oprot.writeFieldEnd()
    if self.expirationTime is not None:
      oprot.writeFieldBegin('expirationTime', TType.I64, 4)
      oprot.writeI64(self.expirationTime)
      oprot.writeFieldEnd()
    if self.priority is not None:
      oprot.writeFieldBegin('priority', TType.DOUBLE, 5)
      oprot.writeDouble(self.priority)
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.STRING, 6)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.version is None:
      raise TProtocol.TProtocolException(message='Required field version is unset!')
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TokenMasterException(TException):
  """
  Attributes:
   - errorCode
   - errorMessage
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'errorCode', None, None, ), # 1
    (2, TType.STRING, 'errorMessage', None, None, ), # 2
  )

  def __init__(self, errorCode=None, errorMessage=None,):
    self.errorCode = errorCode
    self.errorMessage = errorMessage

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.errorCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.errorMessage = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TokenMasterException')
    if self.errorCode is not None:
      oprot.writeFieldBegin('errorCode', TType.I32, 1)
      oprot.writeI32(self.errorCode)
      oprot.writeFieldEnd()
    if self.errorMessage is not None:
      oprot.writeFieldBegin('errorMessage', TType.STRING, 2)
      oprot.writeString(self.errorMessage)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ArchiveRequest:
  """
  Attributes:
   - tokens
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'tokens', (TType.STRUCT,(Token, Token.thrift_spec)), None, ), # 1
  )

  def __init__(self, tokens=None,):
    self.tokens = tokens

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.tokens = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = Token()
            _elem5.read(iprot)
            self.tokens.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ArchiveRequest')
    if self.tokens is not None:
      oprot.writeFieldBegin('tokens', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.tokens))
      for iter6 in self.tokens:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GroupRequest:
  """
  Attributes:
   - namePrefix
   - groupSuffix
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'namePrefix', None, None, ), # 1
    (2, TType.STRING, 'groupSuffix', None, None, ), # 2
  )

  def __init__(self, namePrefix=None, groupSuffix=None,):
    self.namePrefix = namePrefix
    self.groupSuffix = groupSuffix

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.namePrefix = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.groupSuffix = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('GroupRequest')
    if self.namePrefix is not None:
      oprot.writeFieldBegin('namePrefix', TType.STRING, 1)
      oprot.writeString(self.namePrefix)
      oprot.writeFieldEnd()
    if self.groupSuffix is not None:
      oprot.writeFieldBegin('groupSuffix', TType.STRING, 2)
      oprot.writeString(self.groupSuffix)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GroupResponse:
  """
  Attributes:
   - counts
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'counts', (TType.STRING,None,TType.I32,None), None, ), # 1
  )

  def __init__(self, counts=None,):
    self.counts = counts

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.counts = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin() 
          for _i11 in xrange(_size7):
            _key12 = iprot.readString();
            _val13 = iprot.readI32();
            self.counts[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('GroupResponse')
    if self.counts is not None:
      oprot.writeFieldBegin('counts', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.I32, len(self.counts))
      for kiter14,viter15 in self.counts.items():
        oprot.writeString(kiter14)
        oprot.writeI32(viter15)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ModifyRequest:
  """
  Attributes:
   - updates
   - deletes
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'updates', (TType.STRUCT,(Token, Token.thrift_spec)), None, ), # 1
    (2, TType.LIST, 'deletes', (TType.STRUCT,(Token, Token.thrift_spec)), None, ), # 2
  )

  def __init__(self, updates=None, deletes=None,):
    self.updates = updates
    self.deletes = deletes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.updates = []
          (_etype19, _size16) = iprot.readListBegin()
          for _i20 in xrange(_size16):
            _elem21 = Token()
            _elem21.read(iprot)
            self.updates.append(_elem21)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.deletes = []
          (_etype25, _size22) = iprot.readListBegin()
          for _i26 in xrange(_size22):
            _elem27 = Token()
            _elem27.read(iprot)
            self.deletes.append(_elem27)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ModifyRequest')
    if self.updates is not None:
      oprot.writeFieldBegin('updates', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.updates))
      for iter28 in self.updates:
        iter28.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.deletes is not None:
      oprot.writeFieldBegin('deletes', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.deletes))
      for iter29 in self.deletes:
        iter29.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ModifyResponse:
  """
  Attributes:
   - updates
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'updates', (TType.STRUCT,(Token, Token.thrift_spec)), None, ), # 1
  )

  def __init__(self, updates=None,):
    self.updates = updates

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.updates = []
          (_etype33, _size30) = iprot.readListBegin()
          for _i34 in xrange(_size30):
            _elem35 = Token()
            _elem35.read(iprot)
            self.updates.append(_elem35)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ModifyResponse')
    if self.updates is not None:
      oprot.writeFieldBegin('updates', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.updates))
      for iter36 in self.updates:
        iter36.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Query:
  """
  Attributes:
   - namePrefix
   - maxTokens
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'namePrefix', None, None, ), # 1
    (2, TType.I32, 'maxTokens', None, None, ), # 2
  )

  def __init__(self, namePrefix=None, maxTokens=None,):
    self.namePrefix = namePrefix
    self.maxTokens = maxTokens

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.namePrefix = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.maxTokens = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Query')
    if self.namePrefix is not None:
      oprot.writeFieldBegin('namePrefix', TType.STRING, 1)
      oprot.writeString(self.namePrefix)
      oprot.writeFieldEnd()
    if self.maxTokens is not None:
      oprot.writeFieldBegin('maxTokens', TType.I32, 2)
      oprot.writeI32(self.maxTokens)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryRequest:
  """
  Attributes:
   - queries
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'queries', (TType.STRUCT,(Query, Query.thrift_spec)), None, ), # 1
  )

  def __init__(self, queries=None,):
    self.queries = queries

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.queries = []
          (_etype40, _size37) = iprot.readListBegin()
          for _i41 in xrange(_size37):
            _elem42 = Query()
            _elem42.read(iprot)
            self.queries.append(_elem42)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QueryRequest')
    if self.queries is not None:
      oprot.writeFieldBegin('queries', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.queries))
      for iter43 in self.queries:
        iter43.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryResponse:
  """
  Attributes:
   - tokens
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'tokens', (TType.LIST,(TType.STRUCT,(Token, Token.thrift_spec))), None, ), # 1
  )

  def __init__(self, tokens=None,):
    self.tokens = tokens

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.tokens = []
          (_etype47, _size44) = iprot.readListBegin()
          for _i48 in xrange(_size44):
            _elem49 = []
            (_etype53, _size50) = iprot.readListBegin()
            for _i54 in xrange(_size50):
              _elem55 = Token()
              _elem55.read(iprot)
              _elem49.append(_elem55)
            iprot.readListEnd()
            self.tokens.append(_elem49)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QueryResponse')
    if self.tokens is not None:
      oprot.writeFieldBegin('tokens', TType.LIST, 1)
      oprot.writeListBegin(TType.LIST, len(self.tokens))
      for iter56 in self.tokens:
        oprot.writeListBegin(TType.STRUCT, len(iter56))
        for iter57 in iter56:
          iter57.write(oprot)
        oprot.writeListEnd()
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryAndOwnRequest:
  """
  Attributes:
   - owner
   - expirationTime
   - query
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'owner', None, None, ), # 1
    (2, TType.I64, 'expirationTime', None, None, ), # 2
    (3, TType.STRUCT, 'query', (Query, Query.thrift_spec), None, ), # 3
  )

  def __init__(self, owner=None, expirationTime=None, query=None,):
    self.owner = owner
    self.expirationTime = expirationTime
    self.query = query

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.owner = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.expirationTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.query = Query()
          self.query.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QueryAndOwnRequest')
    if self.owner is not None:
      oprot.writeFieldBegin('owner', TType.STRING, 1)
      oprot.writeString(self.owner)
      oprot.writeFieldEnd()
    if self.expirationTime is not None:
      oprot.writeFieldBegin('expirationTime', TType.I64, 2)
      oprot.writeI64(self.expirationTime)
      oprot.writeFieldEnd()
    if self.query is not None:
      oprot.writeFieldBegin('query', TType.STRUCT, 3)
      self.query.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryAndOwnResponse:
  """
  Attributes:
   - tokens
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'tokens', (TType.STRUCT,(Token, Token.thrift_spec)), None, ), # 1
  )

  def __init__(self, tokens=None,):
    self.tokens = tokens

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.tokens = []
          (_etype61, _size58) = iprot.readListBegin()
          for _i62 in xrange(_size58):
            _elem63 = Token()
            _elem63.read(iprot)
            self.tokens.append(_elem63)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QueryAndOwnResponse')
    if self.tokens is not None:
      oprot.writeFieldBegin('tokens', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.tokens))
      for iter64 in self.tokens:
        iter64.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['{0!s}={1!r}'.format(key, value)
      for key, value in self.__dict__.iteritems()]
    return '{0!s}({1!s})'.format(self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
