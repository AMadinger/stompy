#!/usr/bin/env python
"""
Much of this is from the StompyLegControl firmware
make sure it is up to date
"""

ESTOP_OFF = 0
ESTOP_SOFT = 1
ESTOP_HARD = 2
ESTOP_HOLD = 3
ESTOP_ON = 2
ESTOP_HEARTBEAT = 2
ESTOP_DEFAULT = 2

HEARTBEAT_TIMEOUT = 1.0
HEARTBEAT_PERIOD = HEARTBEAT_TIMEOUT / 2.

LEG_NAMES_BY_NUMBER = {
    0: 'Undefined',
    1: 'Front-Left',
    2: 'Middle-Left',
    3: 'Rear-Left',
    4: 'Rear-Right',
    5: 'Middle-Right',
    6: 'Front-Right',
    7: 'Fake',
}

PLAN_STOP_MODE = 0
PLAN_VELOCITY_MODE = 1
PLAN_ARC_MODE = 2
PLAN_TARGET_MODE = 3

PLAN_SENSOR_FRAME = 0
PLAN_JOINT_FRAME = 1
PLAN_LEG_FRAME = 2
PLAN_BODY_FRAME = 3