#!/usr/bin/python
###############################################################################
#                WH Water Detection Sensor for Raspberrypi  
#                      Sensor Analytics Australia™ 2024
###############################################################################
from time import sleep
import os

while True:
    try:
        os.system('python ./wh.py')
    except:
        sleep(30)
        pass
# Uncomment the following lines to allow interruption of the program
#    else:
#        break
