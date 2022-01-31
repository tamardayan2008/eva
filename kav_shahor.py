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
gyro= Port.S4
colorSensor= port.S1

def FL25 (speed, turn_rate, colorSensor):
    if colorSensor.reflection() <= 15:
        drivebase.drive (speed * -1, turn_rate * -1)
    if colorSensor.reflection() <= 15:
        drivebase.drive (speed * -1, turn_rate)
    else:
        drivebase.drive (speed * -1, 0)