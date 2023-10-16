#!/usr/bin/env python3

# Play games until one of them is a winner
import subprocess

games_played = 0
while True:
    result = subprocess.run(['python', 'ginrummy.py', '--pretty-print'])
    games_played += 1
    if result.returncode == 0:
        print("Inner script returned 0. Stopping!")
        print(games_played)
        break
    else:
        pass
        #print(f"Inner script returned {result.returncode}. Running again...")
