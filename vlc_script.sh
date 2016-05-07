#!/usr/bin/env bash
TIME_OUT=${1:-99999}
raspivid -o - -t 99999 -vf -w 640 -h 360 -fps 25|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
