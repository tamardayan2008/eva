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

robot.straight(233) #נוסעת ישר עם המשאית
robot.turn(45) #פונה
robot.straight(313) #מביאה את שתי המשאיות לגשר
tiny_motor.run_angle(100, -90, then=Stop.BRAKE, wait=True) #יוצאת מהמשאית
tiny_motor.stop() #הפסקה
robot.turn(2) #פונה
robot.straight(261) #הולכת לגשר הקרוב
tiny_motor.run_angle(-200, -230, then=Stop.BRAKE, wait=True) #מורידה את הגשר הקרוב
tiny_motor.stop() #הפסקה
robot.turn(1.5) #פונה
robot.straight(200) #נוסעת לגשר הרחוק
tiny_motor.run_angle(-200, 185, then=Stop.BRAKE, wait=True) #מורידה את הגשר הרחוק
tiny_motor.stop() #הפסקה


robot.straight(100) #מתקדמת לעיגול של קרגו קונקט
robot.turn(-60) #פונה
robot.straight(100) #מניחה את המודל חדשנות בתוך העיגול של קרגו קונקט
robot.straight(-55) #יוצאת מהעיגול של קרגו קונקט
robot.turn(40) #פונה
tiny_motor.run_angle(200, 120, then=Stop.BRAKE, wait=True) #זרוע זזה לגובה של המסיל
robot.straight(453) #מתקדמת לרכבת


robot.turn(90) #פונה
robot.straight(40) #מתקדמת למסיל 
#robot.turn(-30) #פונה ומורידה את המסיל

#robot.straight(300) #הולכת למסוק
#robot.turn(40) #פונה כדי שתהיה עם גב למסוק
#robot.straight(-10) #מתנגשת במסוק
#robot.straight(10) #יוצאת מהמסוק

#robot.turn(-40) #פונה לכיוון הרכבת
#tiny_motor.run_angle(200, -170, then=Stop.BRAKE, wait=True) #זרוע זזה כדי שתוכל לדחוף את הרכבת
#robot.straight(600) #דוחפת את הרכבת

#robot.straight(-500) #הולכת אחורה לכיוון המנוף
#robot.turn(90) #פונה לכיוון הבית
#robot.straight(600) #מתקדמת לכיוון הבית
#robot.turn(-30) #פונה לכיוון הבית
#robot.straight(100) #נוסעת הביתה