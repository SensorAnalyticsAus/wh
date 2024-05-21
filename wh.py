#!/usr/bin/python
###############################################################################
#                WH Water Detection Sensor for Raspberrypi  
#                      Sensor Analytics Australia™ 2024
###############################################################################
Mute = 0     # 0 - mute, 1 - enable pushover.net sound alert and alarm 
po_token='your pushover app token'
po_user='your pushover user key'
TolAlert = 15  # every secs 
TolAlarm = 60  # every secs
pin = 11     #physical pin (not gpio no etc) connected to pir's signal wire

import RPi.GPIO as GPIO
import time
from datetime import datetime
import signal,sys
import json,http.client, urllib #for po

def po(msg,snd): #pushover PIR_MD to send msg to mobile, change token and user
 conn = http.client.HTTPSConnection("api.pushover.net:443")
 conn.request("POST", "/1/messages.json",
 urllib.parse.urlencode({
     "token": po_token,
     "user": po_user,
     "sound": snd,
     "message": msg,
     }), { "Content-type": "application/x-www-form-urlencoded" })
 resp=conn.getresponse()
 respobj = json.loads(resp.read())
 json_formatted_str = json.dumps(respobj, indent=4)
 return json_formatted_str
def signal_handler(signal, frame):
 print('\ngotta go...')
 sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print(datetime.now().strftime('%H:%M:%S'),'PIR Motion Detector started...')
print('ctrl-C to exit')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)    
knt=0    
now = datetime.now()
t_i = datetime.timestamp(now)
while True:
    now = datetime.now().strftime("%H:%M:%S")
    now2 = datetime.now()
    t_c = datetime.timestamp(now2)
    i=GPIO.input(pin)
    if i==0:              
        knt+=1
        print (now,'Water Detected',i)
        if knt%TolAlert == 0: 
            msg=now+' Water Detect Alert'
            print(msg)
            if Mute == 1: po(msg,'gamelan')
        if int(t_c-t_i)%TolAlarm == 0: 
            msg=now+' Water Alarm Check Cameras!'
            print(msg)
            if Mute == 1: po(msg,'alarm')
        time.sleep(0.1)
    else: knt=0 # reset counter
    time.sleep(1)
