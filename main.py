#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math

# Write your program here
brick.sound.beep()

gyro = GyroSensor(Port.S2)
motor1 = Motor(Port.B)
motor2 = Motor(Port.C)
robot = DriveBase(motor1, motor2, 56, 50)
gyro.mode = "GYRO-CAL"
gyro.reset_angle(0)

#Must start robot in upright balanced position
while True:
   angle = gyro.speed()
   print(angle)
   #This part actually implements
   if angle > 3:
      robot.drive_time(5*angle+100,0, 200)
   elif angle < -3:
      robot.drive_time(5*angle-100,0,200)
   else:
      robot.stop(Stop.HOLD)
