# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

import numpy as np
from matplotlib import pyplot as plt

with open("input-day5.txt", "r") as f:
    lines = f.readlines()

#input vertalen in leesbaar formaat: list of list of tuples
lines = [line.split(' -> ') for line in lines]
for n, line in enumerate(lines):
    x1 = line[0].split(',')[0]
    y1 = line[0].split(',')[1]
    x2 = line[1].split(',')[0]
    y2 = line[1].split(',')[1]
    lines[n] = [int(i) for i in [x1,y1,x2,y2]]

#%% part 1
# deze functie telt 1 op bij de vakjes van de betreffende lijn
def teken_lijn(line, grid):
    x1, x2 = min([line[0], line[2]]), max([line[0], line[2]])
    y1, y2 = min([line[1], line[3]]), max([line[1], line[3]])
    if x1 == x2 or y1 == y2:
        grid[x1:x2+1, y1:y2+1] += 1
    return grid
 
# leeg grid tekenen    
grid = np.zeros((1000,1000), dtype=int)

# vullen grid met lijnen
for line in lines:
    grid = teken_lijn(line, grid)

unique, counts = np.unique(grid, return_counts=True)
print('het antwoord op part 1 is', np.sum(counts[2:]))

#%% part 2
# we tekenen nu de diagonale lijnen er bij
def teken_diag(line, grid):
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if x1 == x2 or y1 == y2:
        x1, x2 = min(line[0], line[2]), max(line[0], line[2])
        y1, y2 = min(line[1], line[3]), max(line[1], line[3])
        grid[x1:x2+1, y1:y2+1] += 1
    elif abs(x2 - x1) == abs(y2 - y1):
        diag_len = abs(x2-x1)  
        for n in range(diag_len+1):
            inc_x = (x2-x1)/diag_len 
            inc_y = (y2-y1)/diag_len
            #print()
            grid[int(x1+inc_x*n), int(y1+inc_y*n)] += 1
    return grid

# leeg grid tekenen    
grid = np.zeros((1000,1000), dtype=int)

# vullen grid met lijnen
for line in lines:
    grid = teken_diag(line, grid)

unique, counts = np.unique(grid, return_counts=True)
antwoord = sum(counts[2:])

print('het antwoord op part 2 is ', antwoord)
#%% Testdata

lines = ['0,9 -> 5,9',
'8,0 -> 0,8',
'9,4 -> 3,4',
'2,2 -> 2,1',
'7,0 -> 7,4',
'6,4 -> 2,0',
'0,9 -> 2,9',
'3,4 -> 1,4',
'0,0 -> 8,8',
'5,5 -> 8,2']

lines = [line.split(' -> ') for line in lines]
for n, line in enumerate(lines):
    x1 = line[0].split(',')[0]
    y1 = line[0].split(',')[1]
    x2 = line[1].split(',')[0]
    y2 = line[1].split(',')[1]
    lines[n] = [int(i) for i in [x1,y1,x2,y2]]

grid = np.zeros((10,10), dtype=int)

# vullen grid met lijnen
for line in lines:
    grid = teken_diag(line, grid)

unique, counts = np.unique(grid, return_counts=True)
antwoord = sum(counts[2:])

print('het antwoord op de testopgave van deel 2 is ', antwoord)