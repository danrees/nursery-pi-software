#!/usr/bin/env bash

echo Lights off
i2cset -y 1 0x70 0x00 0x00
