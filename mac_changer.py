#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:22:44:66:88:11", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
