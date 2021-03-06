#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def archive(self, request):
    """
    Parameters:
     - request
    """
    pass

  def group(self, request):
    """
    Parameters:
     - request
    """
    pass

  def modify(self, request):
    """
    Parameters:
     - request
    """
    pass

  def query(self, request):
    """
    Parameters:
     - request
    """
    pass

  def query_and_own(self, request):
    """
    Parameters:
     - request
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def archive(self, request):
    """
    Parameters:
     - request
    """
    self.send_archive(request)
    self.recv_archive()

  def send_archive(self, request):
    self._oprot.writeMessageBegin('archive', TMessageType.CALL, self._seqid)
    args = archive_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_archive(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = archive_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.e is not None:
      raise result.e
    return

  def group(self, request):
    """
    Parameters:
     - request
    """
    self.send_group(request)
    return self.recv_group()

  def send_group(self, request):
    self._oprot.writeMessageBegin('group', TMessageType.CALL, self._seqid)
    args = group_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_group(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = group_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "group failed: unknown result");

  def modify(self, request):
    """
    Parameters:
     - request
    """
    self.send_modify(request)
    return self.recv_modify()

  def send_modify(self, request):
    self._oprot.writeMessageBegin('modify', TMessageType.CALL, self._seqid)
    args = modify_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_modify(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = modify_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "modify failed: unknown result");

  def query(self, request):
    """
    Parameters:
     - request
    """
    self.send_query(request)
    return self.recv_query()

  def send_query(self, request):
    self._oprot.writeMessageBegin('query', TMessageType.CALL, self._seqid)
    args = query_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "query failed: unknown result");

  def query_and_own(self, request):
    """
    Parameters:
     - request
    """
    self.send_query_and_own(request)
    return self.recv_query_and_own()

  def send_query_and_own(self, request):
    self._oprot.writeMessageBegin('query_and_own', TMessageType.CALL, self._seqid)
    args = query_and_own_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_query_and_own(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = query_and_own_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.e is not None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "query_and_own failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["archive"] = Processor.process_archive
    self._processMap["group"] = Processor.process_group
    self._processMap["modify"] = Processor.process_modify
    self._processMap["query"] = Processor.process_query
    self._processMap["query_and_own"] = Processor.process_query_and_own

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function {0!s}'.format((name)))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_archive(self, seqid, iprot, oprot):
    args = archive_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = archive_result()
    try:
      self._handler.archive(args.request)
    except TokenMasterException as e:
      result.e = e
    oprot.writeMessageBegin("archive", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_group(self, seqid, iprot, oprot):
    args = group_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = group_result()
    try:
      result.success = self._handler.group(args.request)
    except TokenMasterException as e:
      result.e = e
    oprot.writeMessageBegin("group", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_modify(self, seqid, iprot, oprot):
    args = modify_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = modify_result()
    try:
      result.success = self._handler.modify(args.request)
    except TokenMasterException as e:
      result.e = e
    oprot.writeMessageBegin("modify", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_query(self, seqid, iprot, oprot):
    args = query_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = query_result()
    try:
      result.success = self._handler.query(args.request)
    except TokenMasterException as e:
      result.e = e
    oprot.writeMessageBegin("query", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_query_and_own(self, seqid, iprot, oprot):
    args = query_and_own_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = query_and_own_result()
    try:
      result.success = self._handler.query_and_own(args.request)
    except TokenMasterException as e:
      result.e = e
    oprot.writeMessageBegin("query_and_own", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class archive_args:
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (ArchiveRequest, ArchiveRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
        if ftype == TType.STRUCT:
          self.request = ArchiveRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('archive_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
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

class archive_result:
  """
  Attributes:
   - e
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'e', (TokenMasterException, TokenMasterException.thrift_spec), None, ), # 1
  )

  def __init__(self, e=None,):
    self.e = e

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
        if ftype == TType.STRUCT:
          self.e = TokenMasterException()
          self.e.read(iprot)
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
    oprot.writeStructBegin('archive_result')
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
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

class group_args:
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (GroupRequest, GroupRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
        if ftype == TType.STRUCT:
          self.request = GroupRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('group_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
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

class group_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (GroupResponse, GroupResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (TokenMasterException, TokenMasterException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = GroupResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TokenMasterException()
          self.e.read(iprot)
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
    oprot.writeStructBegin('group_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
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

class modify_args:
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (ModifyRequest, ModifyRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
        if ftype == TType.STRUCT:
          self.request = ModifyRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('modify_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
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

class modify_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (ModifyResponse, ModifyResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (TokenMasterException, TokenMasterException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = ModifyResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TokenMasterException()
          self.e.read(iprot)
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
    oprot.writeStructBegin('modify_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
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

class query_args:
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (QueryRequest, QueryRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
        if ftype == TType.STRUCT:
          self.request = QueryRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('query_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
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

class query_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (QueryResponse, QueryResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (TokenMasterException, TokenMasterException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = QueryResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TokenMasterException()
          self.e.read(iprot)
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
    oprot.writeStructBegin('query_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
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

class query_and_own_args:
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (QueryAndOwnRequest, QueryAndOwnRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

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
        if ftype == TType.STRUCT:
          self.request = QueryAndOwnRequest()
          self.request.read(iprot)
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
    oprot.writeStructBegin('query_and_own_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
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

class query_and_own_result:
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (QueryAndOwnResponse, QueryAndOwnResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'e', (TokenMasterException, TokenMasterException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = QueryAndOwnResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = TokenMasterException()
          self.e.read(iprot)
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
    oprot.writeStructBegin('query_and_own_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.e is not None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
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
