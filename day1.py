# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:11:33 2021

@author: Bouke
"""

from matplotlib import pyplot as plt

#%% part 1
with open("input-day1.txt", "r") as f:
    input = f.readlines()
input = [int(x) for x in input]

count = 0

for n in range(1,len(input)):
    if input[n] > input[n-1]:
        count += 1
        
print("The answer is", count)

x = range(0,len(input))
y = [input[n] for n in x]
plt.plot(x,y)

#%% part 2 
sliding = [sum(input[n-1:n+2]) for n in range(1,len(input)-1)]

count2 = 0

for n in range(1,len(sliding)):
    if sliding[n] > sliding[n-1]:
        count2 += 1
        
print("The answer to part 2 is", count2)