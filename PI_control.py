import PI_pyaudio as pa
import transcribe1106 as tr

#test='/home/sansungyoon/FORcapstone/testFile/Light_off_converted.wav'
test2='/home/sansungyoon/FORcapstone/testFile/Light_on_converted.wav'
#temp=tr.transcribe(test)
temp2=tr.transcribe(test2)
#print temp
#print temp2

light_mode=0

"""
if(temp==u'\ubd88 \uaebc'):
    #print 'light off'
    light_mode=0
"""
if(temp2==u'\ubd88 \ucf1c'):
    #print 'light on'
    light_mode=1


import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.OUT)
GPIO.output(23,False)

if(light_mode==1):
    GPIO.output(23,True)

"""
if(light_mode==0):
    GPIO.output(23,False)
"""

raw_input('press enter to exit program')
GPIO.cleanup()


