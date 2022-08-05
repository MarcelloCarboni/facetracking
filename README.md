# facetracking

This simple project is meant to run on a Raspberry Pi and a Arduino.
For the Raspberry I'm using a Pi Zero W with RaspberryOS, but it's way too slow to actually work.
For the Arduino, I'm using a knockoff Nano v3 (ATmega328).
The script will use opencv2 to find a face in a webcam stream and rotate the webcam to frame the face in the center, using an arduino and a 28BYJ-48 stepper motor with a ULN2003 driver.

This is still a work in progress and should be treated as such.

TODOs:
 - Switch from Haar Cascade algo to HoG.