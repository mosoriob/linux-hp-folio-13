#!/usr/bin/env python
from __future__ import print_function

import time
import subprocess

LID = "/proc/acpi/button/lid/LID0/state"
CLOSED_STATE = "state:      closed\n"
SUSPEND_CMD = "/usr/sbin/pm-suspend"

def suspend_if_closed():
  with open(LID, "r") as f:
    state = f.read()
    if state == CLOSED_STATE:
      print("Lid closed, suspending...")
      subprocess.call(SUSPEND_CMD)

if __name__ == '__main__':
  while True:
    suspend_if_closed()
    time.sleep(1)
    # sleep again... to avoid instant suspend when waking (theoretical)
    time.sleep(1)
