#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,  GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

ev3.speaker.beep()

left_motor= Motor(Port.C) #מנוע ימני
right_motor= Motor(Port.B) #מנוע שמאלי
tiny_motor= Motor(Port.D) #מנוע בינוני

robot= DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=100) #הגדרות נסיעה ישר 
robot.settings(900, 900,  72, 72) #הגדרות מהירות נסיעה

robot.straight(673) #נוסעת אל הברווז עם המכולות 

robot.turn(-6) #פונה לכיוון הברווז
tiny_motor.run_time(-400, 1575, then=Stop.BRAKE, wait=True) #מורידה את הברווז
robot.straight(3) #טיפה קדימה
robot.turn(-8) #פונה טיפה
tiny_motor.run_angle(100, 30, then=Stop.BRAKE, wait=True) #מעלה את הזרוע
robot.turn(8) #פונה טיפה
robot.straight(-8) #נוסעת טיפה אחורה 
tiny_motor.run_time(-600, 1000, then=Stop.BRAKE, wait=True) #מורידה את הזרוע

tiny_motor.run_time(400, 280, then=Stop.BRAKE, wait=True) #מעלה את הזרוע כדי שלא תפריע לה לנסוע
robot.straight(-80) #נוסעת אחורה
robot.turn(57) #פונה לכיוון המכולה שיצאה מהברווז
robot.straight(65) #נוסעת קדימה לכיוון המכולה שיצאה מהברווז
tiny_motor.run_time(-400, 220, then=Stop.BRAKE, wait=True) #מורידה את הזרוע
robot.turn(-45) #מזיזה את המכולה לתוך העיגול

tiny_motor.run_time(400, 180, then=Stop.BRAKE, wait=True) #מעלה את הזרוע כדי שלא תפריע לה לנסוע 
robot.turn(12) #פונה לכיוון המנוע
robot.straight(178) #נוסעת לכיוון הקיר כדי להתיישר עליו
robot.turn(190) #מסתובבת לכיוון הקיר כדי להתיישר עליו
#robot.straight(-400) #מתיישרת על הקיר
#robot.straight(20) #מתקדמת קצת קדימה
#robot.turn(-60) #פונה לכיוון המנוע 
#tiny_motor.run_time(-400, 500, then=Stop.BRAKE, wait=True) #מורידה את הזרוע עד למטה
#robot.turn(6) #פונה לכיוון המנוע 
#tiny_motor.run_angle(400, 200, then=Stop.BRAKE, wait=True) #מסובבת את המנוע

#robot.straight(-40) #נוסעת אחורה
#robot.turn(45) #פונה לכיוון המשימה הבאה
#robot.straight(400) #נוסעת קדימה
#robot.turn(45) #פונה לכיוון המשימה הבאה
#robot.straight(400) #נוסעת לכיוון המשימה הבאה