// Generated by gencpp from file car/OdomVelocities.msg
// DO NOT EDIT!


#ifndef CAR_MESSAGE_ODOMVELOCITIES_H
#define CAR_MESSAGE_ODOMVELOCITIES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace car
{
template <class ContainerAllocator>
struct OdomVelocities_
{
  typedef OdomVelocities_<ContainerAllocator> Type;

  OdomVelocities_()
    : header()
    , v_x(0.0)
    , v_y(0.0)
    , v_psi(0.0)
    , noise_x(0.0)
    , noise_y(0.0)
    , noise_psi(0.0)  {
    }
  OdomVelocities_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , v_x(0.0)
    , v_y(0.0)
    , v_psi(0.0)
    , noise_x(0.0)
    , noise_y(0.0)
    , noise_psi(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef double _v_x_type;
  _v_x_type v_x;

   typedef double _v_y_type;
  _v_y_type v_y;

   typedef double _v_psi_type;
  _v_psi_type v_psi;

   typedef double _noise_x_type;
  _noise_x_type noise_x;

   typedef double _noise_y_type;
  _noise_y_type noise_y;

   typedef double _noise_psi_type;
  _noise_psi_type noise_psi;




  typedef boost::shared_ptr< ::car::OdomVelocities_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::car::OdomVelocities_<ContainerAllocator> const> ConstPtr;

}; // struct OdomVelocities_

typedef ::car::OdomVelocities_<std::allocator<void> > OdomVelocities;

typedef boost::shared_ptr< ::car::OdomVelocities > OdomVelocitiesPtr;
typedef boost::shared_ptr< ::car::OdomVelocities const> OdomVelocitiesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::car::OdomVelocities_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::car::OdomVelocities_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace car

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'car': ['/home/marc/catkin_ws/src/car/msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::car::OdomVelocities_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::car::OdomVelocities_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::car::OdomVelocities_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::car::OdomVelocities_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::car::OdomVelocities_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::car::OdomVelocities_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::car::OdomVelocities_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7af9e375008818dc1ff8fe56d859f851";
  }

  static const char* value(const ::car::OdomVelocities_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7af9e375008818dcULL;
  static const uint64_t static_value2 = 0x1ff8fe56d859f851ULL;
};

template<class ContainerAllocator>
struct DataType< ::car::OdomVelocities_<ContainerAllocator> >
{
  static const char* value()
  {
    return "car/OdomVelocities";
  }

  static const char* value(const ::car::OdomVelocities_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::car::OdomVelocities_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n\
float64 v_x\n\
float64 v_y\n\
float64 v_psi\n\
float64 noise_x\n\
float64 noise_y\n\
float64 noise_psi\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::car::OdomVelocities_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::car::OdomVelocities_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.v_x);
      stream.next(m.v_y);
      stream.next(m.v_psi);
      stream.next(m.noise_x);
      stream.next(m.noise_y);
      stream.next(m.noise_psi);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct OdomVelocities_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::car::OdomVelocities_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::car::OdomVelocities_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "v_x: ";
    Printer<double>::stream(s, indent + "  ", v.v_x);
    s << indent << "v_y: ";
    Printer<double>::stream(s, indent + "  ", v.v_y);
    s << indent << "v_psi: ";
    Printer<double>::stream(s, indent + "  ", v.v_psi);
    s << indent << "noise_x: ";
    Printer<double>::stream(s, indent + "  ", v.noise_x);
    s << indent << "noise_y: ";
    Printer<double>::stream(s, indent + "  ", v.noise_y);
    s << indent << "noise_psi: ";
    Printer<double>::stream(s, indent + "  ", v.noise_psi);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CAR_MESSAGE_ODOMVELOCITIES_H