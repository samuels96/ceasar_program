import sys
import time

def slow_print(s,t=0.04):
    for x in s:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(t)
