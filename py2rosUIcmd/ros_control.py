import rospy
from random import random
from geometry_msgs.msg import Twist

class ROSControl:
    """Control the rotob with differencial drive using ROS cmd_vel topic
    """

    def __init__(self, topic):
        self._topic = topic
        self._publisher = rospy.Publisher('/%s/cmd_vel' % topic,
                                          Twist, queue_size=8)

    def __repr__(self):
        return 'ROSControl(%s)' % self._topic

    def main_loop(self, *args):
        self.set_vel(random(), 1 - 2 * random());
        return True

    def set_vel(self, linear, angular):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        rospy.loginfo(msg)
        self._publisher.publish(msg)

    def start(self, timeout=1):
        rospy.init_node('roscontrol', anonymous=True)
        rospy.Timer(rospy.Duration(timeout), self.main_loop)
        rospy.spin()


if __name__ == '__main__':
    ROSControl('pioneer2dx').start()
