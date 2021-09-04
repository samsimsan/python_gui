# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:11:00 2021

@author: LEOS-7
"""

from sampyapt import APTMotor
import time

#create a 
m1 = APTMotor()
print('creating the instance')
# take the serial number 
a = m1.getSerialNumberByIdx(0)
print('got the serial number')
b = int(str(a)[7:-1])
# set the serial number:
m1.setSerialNumber(b)
# initialize the hardware to form the connections 
print('initializing the motor')
m1.initializeHardwareDevice()
print('initialised the motor')
# m1.getPos()
# print('moving relactive 10')
# m1.mRel(10)
# time.sleep(1)
# print('moving relative -10')
# m1.mRel(-10)
# time.sleep(1)
# print('closing the connection')


#close the port connections to the motor
# m1.cleanUpAPT()
# print('connectins closed')