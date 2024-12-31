#!/usr/bin/python3

"""
  dd.py
  dd.py provides a wrapper around the standard
  dd command to provide status updates.

  Author: Ricky Hewitt <ricky@rickyhewitt.dev>

  License: GNU GPL v3 <http://www.gnu.org>
"""

import subprocess
import time
import sys
import shutil
import platform

def main(*args, **kwargs):
    dd_bin = shutil.which("dd")
    ddargs = args[0]
    ddargs.insert(0, dd_bin)
    pipe = subprocess.Popen(ddargs, shell=False, executable=dd_bin)

    while(1):
      # Detect OS.
      # MacOS (Darwin) uses the -INFO signal
      # Linux uses -USR1
      if platform.system() == 'Darwin':
          output = subprocess.call("kill -INFO %s" % pipe.pid, shell=True)
      else:
          output = subprocess.call("kill -USR1 %s" % pipe.pid, shell=True)

      if pipe.poll() is None:
          time.sleep(1)
      else:
          return pipe.poll()

main([i for i in sys.argv[1:]])
