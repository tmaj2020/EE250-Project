import time
import sys
import grovepi
from grove_rgb_lcd import *
import os

rotaryPort = 0 #Grovepi potentiometer connected to analog port A0
ultrasonicPort = 4 #Grovepi ultrasonic ranger connected to port D4.
LCDPort = 3 #Grovepi LCD panel connected to i2c port 3.
sendNotif = True

grovepi.pinMode(rotaryPort, "INPUT")
grovepi.pinMode(LCDPort, "OUTPUT")

if __name__ == '__main__':
  while (True):
    time.sleep(.1)

    # Set a threshold distance by turning the rotary angle sensor.
    threshold = grovepi.analogRead(rotaryPort)

    # Measures the distance to an object using the ultrasonic ranger.
    distance = grovepi.ultrasonicRead(ultrasonicPort)

    # Determines whether the object is within the threshold distance.
    if (threshold <= distance): # object not wihtin threshold; backlight green
        setText_norefresh(str(threshold)+ "cm             \n" + str(distance) + "cm")
        setRGB(255, 0, 0)
        if (sendNotif):
                os.system("sendmail -t securenotifs@gmail.com < email.txt")
                sendNotif = False
    else: # object within threshold; backlight red
        setText_norefresh(str(threshold)+ "cm OBJ PRES \n" + str(distance) + "cm")
        setRGB(0, 255, 0)
        sendNotif = True
