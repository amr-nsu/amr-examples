import math
import rospy
from random import random
from nav_msgs.msg import Odometry

class ROSOdometry:
    """Get robot odometry from ROS using odom topic
    """

    def __init__(self, topic):
        self._topic = topic
        rospy.Subscriber('/%s/odom' % topic, Odometry, self.odometry_callback)

    def __repr__(self):
        return 'ROSOdometry(%s)' % self._topic

    def coordinates_callback(self, X):
        print('x:%4.2f y:%4.2f psi:%4.2f' % X)

    def odometry_callback(self, data):
#        rospy.loginfo(data)
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        psi = data.pose.pose.orientation.z * math.pi/2.
        self.coordinates_callback((x, y, psi))
        return True

    def start(self, timeout=1):
        rospy.init_node('rosodometry', anonymous=True)
        rospy.spin()


if __name__ == '__main__':
    ROSOdometry('pioneer2dx').start()
