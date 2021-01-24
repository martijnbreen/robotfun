#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

leftMotor = Motor(Port.A)
rightMotor = Motor(Port.B)
pushButton = TouchSensor(Port.S4)

speed = -500
activated = False
counter = 0
while True:
    if pushButton.pressed() == True:
        activated = True
        print( "activated" )

    if activated == True:
        counter += 1
        leftMotor.run( speed )
        rightMotor.run( speed )
        if counter > 30:
            speed = speed * -1
            counter = 0
            activated = False
            leftMotor.stop()
            rightMotor.stop()
            print( "deactivated" )
    time.sleep( 0.1 )

