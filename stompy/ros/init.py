#!/usr/bin/env python

import rospy

from . import clock
from . import joints
from . import legs


def init(name=None):
    if name is None:
        name = 'stompy_control'
    rospy.init_node(name, anonymous=True)
    joints.connect_to_joint_states()
    legs.connect_to_leg_publishers()
    clock.connect()


def init_leg(name=None):
    if name is None:
        name = 'fr'
    rospy.init_node(name, anonymous=True)
    # connect to master
    # setup joint publishers
    # setup trajectory action server
