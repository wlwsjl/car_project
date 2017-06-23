# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from localization_msgs/TransformedMapDense.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import nav_msgs.msg
import geometry_msgs.msg
import localization_msgs.msg
import sensor_msgs.msg
import genpy
import std_msgs.msg

class TransformedMapDense(genpy.Message):
  _md5sum = "378309153e98d7add0d6a551d203ad70"
  _type = "localization_msgs/TransformedMapDense"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
localization_msgs/MapDense map
localization_msgs/Pose2DWithCovarianceStamped transform
bool valid
float64 corr_rotation
float64 corr_translation

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: localization_msgs/MapDense
nav_msgs/MapMetaData metadata
sensor_msgs/Image image
std_msgs/Bool valid

================================================================================
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Bool
bool data
================================================================================
MSG: localization_msgs/Pose2DWithCovarianceStamped
std_msgs/Header header
geometry_msgs/Pose2D pose
float64[9] covariance

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta"""
  __slots__ = ['header','map','transform','valid','corr_rotation','corr_translation']
  _slot_types = ['std_msgs/Header','localization_msgs/MapDense','localization_msgs/Pose2DWithCovarianceStamped','bool','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,map,transform,valid,corr_rotation,corr_translation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TransformedMapDense, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.map is None:
        self.map = localization_msgs.msg.MapDense()
      if self.transform is None:
        self.transform = localization_msgs.msg.Pose2DWithCovarianceStamped()
      if self.valid is None:
        self.valid = False
      if self.corr_rotation is None:
        self.corr_rotation = 0.
      if self.corr_translation is None:
        self.corr_translation = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.map = localization_msgs.msg.MapDense()
      self.transform = localization_msgs.msg.Pose2DWithCovarianceStamped()
      self.valid = False
      self.corr_rotation = 0.
      self.corr_translation = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2If2I7d3I().pack(_x.map.metadata.map_load_time.secs, _x.map.metadata.map_load_time.nsecs, _x.map.metadata.resolution, _x.map.metadata.width, _x.map.metadata.height, _x.map.metadata.origin.position.x, _x.map.metadata.origin.position.y, _x.map.metadata.origin.position.z, _x.map.metadata.origin.orientation.x, _x.map.metadata.origin.orientation.y, _x.map.metadata.origin.orientation.z, _x.map.metadata.origin.orientation.w, _x.map.image.header.seq, _x.map.image.header.stamp.secs, _x.map.image.header.stamp.nsecs))
      _x = self.map.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.map.image.height, _x.map.image.width))
      _x = self.map.image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.map.image.is_bigendian, _x.map.image.step))
      _x = self.map.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_B3I().pack(_x.map.valid.data, _x.transform.header.seq, _x.transform.header.stamp.secs, _x.transform.header.stamp.nsecs))
      _x = self.transform.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.transform.pose.x, _x.transform.pose.y, _x.transform.pose.theta))
      buff.write(_get_struct_9d().pack(*self.transform.covariance))
      _x = self
      buff.write(_get_struct_B2d().pack(_x.valid, _x.corr_rotation, _x.corr_translation))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.map is None:
        self.map = localization_msgs.msg.MapDense()
      if self.transform is None:
        self.transform = localization_msgs.msg.Pose2DWithCovarianceStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.map.metadata.map_load_time.secs, _x.map.metadata.map_load_time.nsecs, _x.map.metadata.resolution, _x.map.metadata.width, _x.map.metadata.height, _x.map.metadata.origin.position.x, _x.map.metadata.origin.position.y, _x.map.metadata.origin.position.z, _x.map.metadata.origin.orientation.x, _x.map.metadata.origin.orientation.y, _x.map.metadata.origin.orientation.z, _x.map.metadata.origin.orientation.w, _x.map.image.header.seq, _x.map.image.header.stamp.secs, _x.map.image.header.stamp.nsecs,) = _get_struct_2If2I7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.map.image.height, _x.map.image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.image.encoding = str[start:end].decode('utf-8')
      else:
        self.map.image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.map.image.is_bigendian, _x.map.image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.map.image.data = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.map.valid.data, _x.transform.header.seq, _x.transform.header.stamp.secs, _x.transform.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      self.map.valid.data = bool(self.map.valid.data)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.transform.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.transform.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.transform.pose.x, _x.transform.pose.y, _x.transform.pose.theta,) = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 72
      self.transform.covariance = _get_struct_9d().unpack(str[start:end])
      _x = self
      start = end
      end += 17
      (_x.valid, _x.corr_rotation, _x.corr_translation,) = _get_struct_B2d().unpack(str[start:end])
      self.valid = bool(self.valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2If2I7d3I().pack(_x.map.metadata.map_load_time.secs, _x.map.metadata.map_load_time.nsecs, _x.map.metadata.resolution, _x.map.metadata.width, _x.map.metadata.height, _x.map.metadata.origin.position.x, _x.map.metadata.origin.position.y, _x.map.metadata.origin.position.z, _x.map.metadata.origin.orientation.x, _x.map.metadata.origin.orientation.y, _x.map.metadata.origin.orientation.z, _x.map.metadata.origin.orientation.w, _x.map.image.header.seq, _x.map.image.header.stamp.secs, _x.map.image.header.stamp.nsecs))
      _x = self.map.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.map.image.height, _x.map.image.width))
      _x = self.map.image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.map.image.is_bigendian, _x.map.image.step))
      _x = self.map.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_B3I().pack(_x.map.valid.data, _x.transform.header.seq, _x.transform.header.stamp.secs, _x.transform.header.stamp.nsecs))
      _x = self.transform.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3d().pack(_x.transform.pose.x, _x.transform.pose.y, _x.transform.pose.theta))
      buff.write(self.transform.covariance.tostring())
      _x = self
      buff.write(_get_struct_B2d().pack(_x.valid, _x.corr_rotation, _x.corr_translation))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.map is None:
        self.map = localization_msgs.msg.MapDense()
      if self.transform is None:
        self.transform = localization_msgs.msg.Pose2DWithCovarianceStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.map.metadata.map_load_time.secs, _x.map.metadata.map_load_time.nsecs, _x.map.metadata.resolution, _x.map.metadata.width, _x.map.metadata.height, _x.map.metadata.origin.position.x, _x.map.metadata.origin.position.y, _x.map.metadata.origin.position.z, _x.map.metadata.origin.orientation.x, _x.map.metadata.origin.orientation.y, _x.map.metadata.origin.orientation.z, _x.map.metadata.origin.orientation.w, _x.map.image.header.seq, _x.map.image.header.stamp.secs, _x.map.image.header.stamp.nsecs,) = _get_struct_2If2I7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.map.image.height, _x.map.image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.image.encoding = str[start:end].decode('utf-8')
      else:
        self.map.image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.map.image.is_bigendian, _x.map.image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.map.image.data = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.map.valid.data, _x.transform.header.seq, _x.transform.header.stamp.secs, _x.transform.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      self.map.valid.data = bool(self.map.valid.data)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.transform.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.transform.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.transform.pose.x, _x.transform.pose.y, _x.transform.pose.theta,) = _get_struct_3d().unpack(str[start:end])
      start = end
      end += 72
      self.transform.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
      _x = self
      start = end
      end += 17
      (_x.valid, _x.corr_rotation, _x.corr_translation,) = _get_struct_B2d().unpack(str[start:end])
      self.valid = bool(self.valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
_struct_9d = None
def _get_struct_9d():
    global _struct_9d
    if _struct_9d is None:
        _struct_9d = struct.Struct("<9d")
    return _struct_9d
_struct_2If2I7d3I = None
def _get_struct_2If2I7d3I():
    global _struct_2If2I7d3I
    if _struct_2If2I7d3I is None:
        _struct_2If2I7d3I = struct.Struct("<2If2I7d3I")
    return _struct_2If2I7d3I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B3I = None
def _get_struct_B3I():
    global _struct_B3I
    if _struct_B3I is None:
        _struct_B3I = struct.Struct("<B3I")
    return _struct_B3I
_struct_B2d = None
def _get_struct_B2d():
    global _struct_B2d
    if _struct_B2d is None:
        _struct_B2d = struct.Struct("<B2d")
    return _struct_B2d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d