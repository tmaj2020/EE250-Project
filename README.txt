Group Members---------------------------
 - Yaoyue Wang
 - Ty Benjamin Majam
----------------------------------------

Project Description---------------------
This project is dedicated to the EE250 final project assignment.

To reflect the concept of node to node communication, we're going to refer back to
one of our previous projects in the use of the grove.py sensors lab where we used a
rangefinder to detect when an object was in a specific range from the sensor. We'll
have this version of our rpi setup communicate with our laptops via some kind of
notification system (through email in our case).

The sensor itself will be collecting data so long as it is powered (data collection)
and will even be able to discern when someone has entered a room before sending out
an email in accordance with its intended function. This is done by having the program
write a command to the system to send a preset email, which is outlined by our 
email.txt file included in this repository (feel free to change the email.txt file to
try having the equipment fulfill some other purpose or display some other message).
------------------------------------------

Instruction Manual------------------------

Python libraries used:
- time
- sys
- grovepi
- grove_rgb_lcd
- os

** It's also important to note that we had to configure a postfix server to run on our
rpi in order to get the email to send to the appropriate gmail account. The video we
used to assist in setting up this server can be found below **
https://www.youtube.com/watch?v=BkVHckJXibE

Physical Components Required:
- Raspberry PI 4
- GrovePi Shield
- GrovePi Ultrasonic Rangefinder
- GrovePi RGB LCD
- GrovePi Potentiometer
** The arrangement of the GrovePi components and what ports are being used can be found 
written into the comments of the SecureSensor.py code **

In order to utilize our program, we have a file titled SecureSensor.py which should
be the only required program to run once postfix has been appropriately configured.
-------------------------------------------
