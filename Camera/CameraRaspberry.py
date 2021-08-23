# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:58:18 2021

@author: edwin
"""

from picamera import PiCamera
from time import sleep
camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image1.jpg')
camera.stop_preview()