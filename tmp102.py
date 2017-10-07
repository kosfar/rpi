#!/usr/bin/env python

import smbus
import time
from datetime import datetime
 
bus = smbus.SMBus(1)
data = bus.read_i2c_block_data(0x48, 0)
msb = data[0]
lsb = data[1]

print (((msb << 8) | lsb) >> 4) * 0.0625      #printing the temperature value in Celsius.

#target = open('/tmp/temp.txt', 'a')
#target.write("%s,%s\n" % ( (((msb << 8) | lsb) >> 4) * 0.0625, datetime.now().strftime('%Y-%m-%d %H:%M:%S') ) )
