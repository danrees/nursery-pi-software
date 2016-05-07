#!/usr/bin/env python3

import BrightPiLed
import time

print("Testing the lights")

for x in range(0, 10):
    print('Counting down {}'.format(x) );
    time.sleep(1);

try:
    light = BrightPiLed.BrightPI(1)
    light.Reset();

