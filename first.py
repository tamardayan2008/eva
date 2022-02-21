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
robot.settings(800, 800,  72, 72) #הגדרות מהירות נסיעה

robot.straight(218) #נוסעת ישר עם המשאית
robot.turn(54.6) #פונה
robot.straight(440) #מביאה את שתי המשאיות לגשר
tiny_motor.run_angle(100, -85, then=Stop.BRAKE, wait=True) #יוצאת מהמשאית
robot.turn(2) #פונה
tiny_motor.stop() #הפסקה
robot.straight(261) #הולכת לגשר הקרוב
robot.turn(3) #פונה
tiny_motor.run_angle(-200, -230, then=Stop.BRAKE, wait=True) #מורידה את הגשר הקרוב
tiny_motor.stop() #הפסקה
robot.turn(1.5) #פונה
robot.straight(200) #נוסעת לגשר הרחוק
tiny_motor.run_angle(-200, 189, then=Stop.BRAKE, wait=True) #מורידה את הגשר הרחוק
tiny_motor.stop() #הפסקה
robot.turn(0.5) #פונה
tiny_motor.stop() #הפסקה


robot.straight(90) #מתקדמת לעיגול של קרגו קונקט
robot.turn(-60) #פונה
robot.straight(130) #מניחה את שמעון בתוך העיגול של קרגו קונקט
tiny_motor.run_angle(200, 120, then=Stop.BRAKE, wait=True) #זרוע זזה לגובה של המסיל
robot.straight(-67) #יוצאת מהעיגול של קרגו קונקט
robot.turn(-26) #פונה
robot.straight(-360) #מתיישרת
tiny_motor.stop() #הפסקה
wait(200) #דיליי


robot.straight(242) #מתקדמת ישר לכיוון של המסיל
robot.turn(45.3) #פונה
robot.straight(100) #מתקדמת למסיל 
robot.turn(30) #פונה
robot.straight(258)#מתקדמת למסיל
robot.turn(25) #פונה
tiny_motor.stop() #הפסקה
robot.straight(53) #מתקדמת למסיל
tiny_motor.run_angle(-300, 165, then=Stop.BRAKE, wait=True) #זזת יד
tiny_motor.stop() #הפסקה
robot.straight(-83) #מורידה את המסיל


tiny_motor.run_angle(300, 160, then=Stop.BRAKE, wait=True) #זזת יד
tiny_motor.stop() #הפסקה
robot.turn(80) #פונה
robot.straight(-92) #הולכת אחורה לכיוון המנוף
robot.turn(-23) #פונה
robot.straight(-360) #הולכת אחורה לכיוון המנוף
robot.turn(54) #פונה
robot.straight(-90) #עושה את המשימה המשותפת
tiny_motor.stop() #הפסקה
wait(200) #דיליי

#robot.straight(40) #הולכת למסוק
#robot.turn(-40) #פונה כדי שתהיה עם גב למסוק
#robot.straight(30) #מתנגשת במסוק

#robot.straight(-550) #
#tiny_motor.run_angle(-300, 200, then=Stop.BRAKE, wait=True) #זזת יד
#robot.turn(-50) #פונה
#robot.straight(70) #
#robot.turn(30) #פונה
#robot.straight(100) #

#tiny_motor.run_angle(300, 100, then=Stop.BRAKE, wait=True) #זזת יד
#robot.straight(300) #
#tiny_motor.stop() #הפסקה
#robot.straight(-300) #

#robot.turn(-40) #פונה לכיוון הרכבת
#tiny_motor.run_angle(200, -170, then=Stop.BRAKE, wait=True) #זרוע זזה כדי שתוכל לדחוף את הרכבת
#robot.straight(600) #דוחפת את הרכבת

#robot.straight(-500) #הולכת אחורה לכיוון המנוף
#robot.turn(90) #פונה לכיוון הבית
#robot.straight(600) #מתקדמת לכיוון הבית
#robot.turn(-30) #פונה לכיוון הבית
#robot.straight(100) #נוסעת הביתה