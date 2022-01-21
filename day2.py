# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

from matplotlib import pyplot as plt

with open("input-day2.txt", "r") as f:
    input = f.readlines()

log = []

#%% part 1    
depth = 0
horizontal_position = 0
    
for move in input:
    if "forward" in move:
        horizontal_position += int(move.split()[1])
    elif "down" in move:
        depth += int(move.split()[1])
    elif "up" in move:
        depth -= int(move.split()[1])
    log.append((horizontal_position, depth))

x= range(0,len(input))
h = [item[0] for item in log]
d = [item[1] for item in log]
plt.plot(x,h)
plt.plot(x,d)
plt.title("Track Day 2 - part 1")

print("The answer to part 1 is", depth*horizontal_position)

#%%% part 2
with open("input-day2.txt", "r") as f:
    input = f.readlines()
log = []

depth = 0
horizontal_position = 0
aim = 0
    
for move in input:
    if "forward" in move:
        horizontal_position += int(move.split()[1])
        depth += (aim*int(move.split()[1]))
    elif "down" in move:
        aim += int(move.split()[1])
    elif "up" in move:
        aim -= int(move.split()[1])
    log.append((horizontal_position, depth))

x = [item[0] for item in log]
y = [item[1] for item in log]
plt.plot(x,y)

print("The answer to part 2 is", depth*horizontal_position)