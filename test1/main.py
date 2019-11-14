#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

# Initialize two motors with default settings on Port B and Port C.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# The wheel diameter of the Robot Educator is 56 millimeters.
# The distance between wheels (axle_track) is 114 millimeters.
wheel_diameter = 56
axle_track = 114
# Create a DriveBase object. The wheel_diameter and axle_track values are
# needed to move robot correct speed/distance when you give drive commands.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# This drives at 100 mm/sec straight
# drive(speed, steering) 
#robot.drive (1, 0)
# This drives straight backwards at 500 mm/sec for 2 seconds
#robot.drive_time(10, 0, 2000) 

# Drive forward at 100 mm/s for two seconds
robot.drive_time(100, 45, 2000)
# Turn at 45 deg/s for three seconds
#robot.drive_time(0, 45, 3000)


brick.sound.beep()