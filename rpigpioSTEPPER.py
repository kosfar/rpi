#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import argparse

parser = argparse.ArgumentParser(description='This is a demo')
parser.add_argument('-m','--mode', help='up or down',required=True)
parser.add_argument('-d','--distance',help='Distance', required=True)
parser.add_argument('-r','--radius',help='Radius', required=True)
parser.add_argument('-p','--percent',help='percent', required=True)
args = parser.parse_args()
 

percent = args.percent
mode = args.mode
distance = float(args.distance) * float(args.percent)
radius = args.radius

# 15: orange
# 13: yellow
# 16: pink
# 11: blue

PINS = [15,13,16,11]

SEQA = [(15,),(15,13),(13,),(13,16),(16,),(16,11),(11,),(11,15)]
RSEQA = [(11,),(11,16),(16,),(16,13),(13,),(13,15),(15,),(15,11)]

DELAY = 0.002

GPIO.setmode(GPIO.BOARD)

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)

def stepper(sequence, pins):
    for step in sequence:
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH) if pin in step else GPIO.output(pin, GPIO.LOW)
        time.sleep(DELAY)

cycle_dist = 2.0 * 3.14 * float(radius)
degrees = (float(distance) / cycle_dist) * 360
internal_steps = (degrees / 5.625) * 64
sbaroi = int(internal_steps / 8)

if mode == 'up':
    for _ in xrange(sbaroi):
        stepper(SEQA,PINS)  # forward
elif mode == 'down':
    for _ in xrange(sbaroi):
        stepper(RSEQA,PINS)  # reverse

#GPIO.cleanup()
