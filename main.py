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
robot.settings(900, 900,  85, 85)

robot.straight(261) #נוסעת ישר עם המשאית
robot.turn(40) #פונה
robot.straight(252) #מביאה את שתי המשאיות לגשר
tiny_motor.run_angle(200, 35, then=Stop.BRAKE, wait=True) #יוצאת מהמשאית
tiny_motor.stop() #הפסקה
robot.straight(250) #הולכת לגשר הקרוב
tiny_motor.run_angle(-200, -215, then=Stop.BRAKE, wait=True) #מורידה את הגשר הקרוב
tiny_motor.stop() #הפסקה
robot.straight(200) #נוסעת לגשר הרחוק
robot.turn(1) #פונה
tiny_motor.run_angle(-200, 185, then=Stop.BRAKE, wait=True) #מורידה את הגשר הרחוק
tiny_motor.stop() #הפסקה

robot.straight(70) #מתקדמת לעיגול של קרגו קונקט
tiny_motor.run_angle(200, 160, then=Stop.BRAKE, wait=True) #מזיזה את היד כדי שתהיה מוכנה לרכבת
