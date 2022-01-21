# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import time

with open("input-day9.txt", "r") as f:
    input = f.readlines()
input = np.array([[int(letter) for letter in line.strip()] for line in input])

#%% part 1    
def check_low(row, column, input):
    """Takes a position indicated by row number 
    and the input data, and returns the value if it is 
    a local low point """ 
    x = int(input[row][column])
    try:
        up = int(input[row-1][column]) > x 
    except IndexError:
        up = True
    try:
        down = int(input[row+1][column]) > x 
    except IndexError:
        down = True
    try:
        left = int(input[row][column-1]) > x 
    except IndexError:
        left = True
    try:
        right = int(input[row][column+1]) > x 
    except IndexError:
        right = True    
    if all([up, down, left, right]):
        return x + 1
    else:
        return 0
        
lowest_points = 0
for row in range(len(input)):
    for column in range(len(input[row])):
        lowest_points += check_low(row, column, input)

print("The answer to part 1 is", lowest_points)
#%% part 2

with open("input-day9.txt", "r") as f:
    input = f.readlines()
input = np.array([[int(letter) for letter in line.strip()] for line in input])

def tick_low(row, column, a):
    """Takes a value indicated by x,y coord in the input
    array, and turns it into 10 the value if it is 
    a local low point """ 
    x = int(input[row][column])
    try:
        up = int(input[row-1][column]) > x 
    except IndexError:
        up = True
    try:
        down = int(input[row+1][column]) > x 
    except IndexError:
        down = True
    try:
        left = int(input[row][column-1]) > x 
    except IndexError:
        left = True
    try:
        right = int(input[row][column+1]) > x 
    except IndexError:
        right = True    
    if all([up, down, left, right]):
        a[row, column] = 10
    else:
        pass

def stofzuiger(array, r, c, counter, klaar=False):
    """Takes an array and the current position as r(ow) and c(olumn)
    Takes a count of the size of the current basin.
    Calls itself eventually"""
    if klaar:
        print('Einde bassin, counter is', counter)
    else:
        array[r,c] = 0
        r_new = r + np.randint()
        c_new = r
    
# Make an interpretable image of all the basins and low points
a = input.copy()
for (row, column), value in np.ndenumerate(a):
        tick_low(row, column, a)
a[a<9] = 1
cmap = colors.ListedColormap(['white', 'moccasin', 'brown', 'blue'])
bounds=[-0.5,0.5,8.5,9.5,10.5]
norm = colors.BoundaryNorm(bounds, cmap.N)
plt.figure(figsize=(10,10))
plt.grid(False)
plt.imshow(a[:9, :18], interpolation='nearest', cmap=cmap, norm=norm, origin='lower')

plt.imshow(input, cmap='Greys', vmin=0, vmax=9)

#%%  approach using skimage

