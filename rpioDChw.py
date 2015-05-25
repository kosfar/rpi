#!/usr/bin/env python

import RPIO
from RPIO import PWM as PWM
import time

RPIO.setmode(RPIO.BOARD)

GPIO = 12
CHANNEL = 1

RPIO.setup(GPIO,RPIO.OUT)

# Setup PWM and DMA channel 0
PWM.set_loglevel(PWM.LOG_LEVEL_DEBUG)
PWM.setup()
PWM.init_channel(CHANNEL,20000)
PWM.print_channel(CHANNEL)

RPIO.output(GPIO, False)

def changespeed(current_speed,set_speed,step_size,delay):
  for counter in range (current_speed, set_speed, step_size):
    pwmmotor=int(round(counter*199,-1))
    print(pwmmotor)
    PWM.add_channel_pulse(CHANNEL,GPIO,0,pwmmotor)
    time.sleep(delay)

# Add some pulses to the subcycle
PWM.add_channel_pulse(CHANNEL, GPIO, 0, 0)

changespeed(0,100,1,0.02) # accelerate from 0 to 100% step 1% delay 0.02 S

time.sleep(10)
# Stop PWM for specific GPIO on channel
PWM.clear_channel_gpio(CHANNEL, GPIO)

# Shutdown all PWM and DMA activity
PWM.cleanup()
RPIO.cleanup()

