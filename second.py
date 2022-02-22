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

robot.straight(677) #נוסעת אל הברווז עם המכולות

robot.turn(-5.5) #פונה לכיוון הברווז
tiny_motor.run_time(-400, 1575, then=Stop.BRAKE, wait=True) #מורידה את הברווז
robot.straight(3) #טיפה קדימה
robot.turn(-8) #פונה טיפה
tiny_motor.run_angle(400, 150, then=Stop.BRAKE, wait=True) #מעלה את הזרוע
robot.turn(8) #פונה טיפה
robot.straight(-3) #נוסעת טיפה אחורה
tiny_motor.run_time(-600, 1000, then=Stop.BRAKE, wait=True) #מורידה את הזרוע

tiny_motor.run_time(400, 280, then=Stop.BRAKE, wait=True) #מעלה את הזרוע כדי שלא תפריע לה לנסוע
robot.straight(-80) #נוסעת אחורה
robot.turn(53) #פונה לכיוון המכולה שיצאה מהברווז
robot.straight(70) #נוסעת קדימה לכיוון המכולה שיצאה מהברווז
tiny_motor.run_time(-400, 220, then=Stop.BRAKE, wait=True) #מורידה את הזרוע
robot.turn(-45) #מזיזה את המכולה לתוך העיגול

tiny_motor.run_time(400, 180, then=Stop.BRAKE, wait=True) #מעלה את הזרוע כדי שלא תפריע לה לנסוע
robot.turn(8) #פונה לכיוון המנוע
robot.straight(150) #נוסעת לכיוון המשימה הבאה
robot.turn(53) #פונה לכיוון המשימה הבאה
tiny_motor.run_time(-400, 300, then=Stop.BRAKE, wait=True) #מורידה את הזרוע עד למטה
robot.straight(90.4) #מתקדמת קצת קדימה
tiny_motor.run_time(90, 700, then=Stop.BRAKE, wait=True) #מסובבת את המנוע

robot.straight(-70) #נוסעת לכיוון המשימה הבאה
robot.turn(-45) #פונה לכיוון משימת הסיום
robot.straight(-320) #נוסעת לכיוון המשימה הבאה
robot.turn(-11) #פונה לכיוון התיישרות על הקיר
robot.straight(-600) #מתיישרת על הקיר
tiny_motor.stop() #הפסקה
wait(200) #דיליי
robot.straight(545) #מתקדמת לכיוון משימת הסיום
robot.turn(85) #פונה בין המטוס למשאית
robot.straight(290) #מתקדמת לכיוון משימת הסיום
robot.turn(-28) #פונה לכיוון המשימה האחרונה
robot.straight(550) #מתקדמת לכיוון משימת הסיום
robot.turn(-86) #פונה לכיוון המשימה האחרונה
robot.straight(200) #מתקדמת לכיוון משימת הסיום

robot.turn(-35) #פונה לכיוון המשימה האחרונה
robot.straight(178) #מתקדמת לכיוון משימת הסיום