#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

left_motor= Motor(Port.C)
right_motor= Motor(Port.D)
tiny_motor= Motor(Port.B)
gyro= GyroSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, 56.0, 100.0)
robot.settings(1000, 1000,  90, 90)

robot.straight(200) #נוסעת אל התיבה
robot.turn(40) #פונה לכיוון איזור הבית
robot.straight(80) #נוסעת אל איזור הבית