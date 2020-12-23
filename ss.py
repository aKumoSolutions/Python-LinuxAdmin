#!/usr/bin/env python

# A system port information gathering script
import subprocess

def ss_func():
    command = "ss"
    command_arg = "-tlpn"
    print ("Gathering System Port Information with %s command:\n" % command)
    subprocess.call([command, command_arg])

ss_func()
