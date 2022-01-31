#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,  GyroSensor)
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
right_motor= Motor(Port.B)
tiny_motor= Motor(Port.D)
gyro= GyroSensor(Port.S4)

robot= DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=100)
robot.settings(900, 900,  85, 85)

robot.straight(233) #נוסעת ישר לכיוון הברווז 
robot.turn(-40) #פונה
tiny_motor.run_angle(100, -300, then=Stop.BRAKE, wait=True) #מוציאה את המכולה מהברווז
robot.straight(-60) #נוסעת אחורה 
robot.turn(80) #פונה

tiny_motor.run_angle(100, -300, then=Stop.BRAKE, wait=True) #מזיזה את הזרוע לגובה של המנוע
robot.straight(120) #נוסעת למנוע שמתחלף 
tiny_motor.run_angle(100, -300, then=Stop.BRAKE, wait=True) #מסובבת את המנוע
robot.straight(-180) #נוסעת אחורה
robot.turn(45) #פונה
robot.straight(300) #נוסעת לכיוון האונייה
robot.turn(-90) #פונה
robot.straight(190) #נוסעת לאונייה

tiny_motor.run_angle(100, -300, then=Stop.BRAKE, wait=True) #מורידה את המכולות
robot.straight(-20) #נוסעת אחורה
robot.turn(90) #פונה

robot.straight(80) #מזיזה את הספינה
robot.straight(-160) #נוסעת אחורה
robot.turn(-90) #פונה
robot.straight(60) #נוסעת קדימה
robot.turn(-90) #פונה
robot.straight(70) #נוסעת למשימה האחרונה