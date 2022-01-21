# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

from matplotlib import pyplot as plt

with open("input-day7.txt", "r") as f:
    input = f.readlines()
input = [int(crab) for crab in input[0].split(',')]

# histogram of crab positions
from matplotlib import pyplot as plt
plt.hist(input)

#%% part 1    

def evaluate_position(position, input):
    fuel_use = 0
    for crab in input:
        fuel_use += abs(crab-position)
    return fuel_use

fuel_use_per_position = [evaluate_position(n, input) for n in range(max(input))]
plt.plot(list(range(max(input))), fuel_use_per_position)

print("The answer to part 1 is", min(fuel_use_per_position))
#%% part 2
with open("input-day7.txt", "r") as f:
    input = f.readlines()
input = [int(crab) for crab in input[0].split(',')]

def evaluate_position2(position, input):
    fuel_use = 0
    for crab in input:
        fuel_use += sum(list(range(abs(crab-position)+1)))
    return fuel_use

fuel_use_per_position = [evaluate_position2(n, input) for n in range(max(input))]
plt.plot(list(range(max(input))), fuel_use_per_position)

print("The answer to part 2 is", min(fuel_use_per_position))