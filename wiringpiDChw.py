#!/usr/bin/env python
import wiringpi2 as wiringpi
from time import sleep

# using P1 header pin numbers  
wiringpi.wiringPiSetupPhys()  
pwmpin = 12

# 0: INPUT
# 1: OUTPUT
# 2: PWM_OUTPUT.
wiringpi.pinMode(pwmpin,2)      # pwm only works on P1 header pin 12  
wiringpi.pwmWrite(pwmpin, 0)    # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

  
pause_time = 0.002          # you can change this to slow down/speed up  
  
try:  
    while True:  
        for i in range(0,1025):
            wiringpi.pwmWrite(pwmpin,i)  
            sleep(pause_time)  
        for i in range(1024,-1,-1):
            wiringpi.pwmWrite(pwmpin,i)  
            sleep(pause_time)  
  
finally:  
    wiringpi.pwmWrite(pwmpin,0)
    wiringpi.pinMode(pwmpin,0)
