#!/usr/bin/env python3

# Play games until one of them is a winner
import subprocess

while True:
    result = subprocess.run(['python', 'ginrummy.py', '--pretty-print'])
    if result.returncode == 0:
        print("Inner script returned 0. Stopping!")
        break
    else:
        pass
        #print(f"Inner script returned {result.returncode}. Running again...")
