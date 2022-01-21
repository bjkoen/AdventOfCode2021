# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 11:09:21 2021

@author: Bouke
"""

import numpy as np
from matplotlib import pyplot as plt

#echte input
# with open("input-day13.txt", "r") as f:
#     input = f.readlines()
with open("test_input-day13.txt", "r") as f:
    input = f.readlines()

# eerst input vertalen in 1) list van alle dots en 2) list van folding instructions
dots = []
fold_instructions = []
for line in input:
    if ',' in line: 
        dots.append([int(a) for a in line.split(',')])
    if 'fold' in line:
        axis,number = line.split()[2].split('=')
        fold_instructions.append((axis,int(number)))
del number, input, line, f, axis

#%% object oriented approach
class Paper:
  def __init__(self, dots): # initialize paper from list of (x,y) coordinates of dots
    xmax,ymax = max([dot[0] for dot in dots]), max([dot[1] for dot in dots])
    self.gridsize = (xmax+1, ymax+1)
    self.array = np.zeros(self.gridsize)
    for x,y in dots:
      self.array[x,y] = 1
       
  def show(self, c='blue'):
    x,y = np.where(self.array >= 1)[0], np.where(self.array>= 1)[1]
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(-1, self.gridsize[0])
    plt.ylim(-1, self.gridsize[1])
    plt.scatter(x,y, marker=".", c=c)
#    plt.axhline(y=7, c='red')

  def fold(self):
    
        

#%%%%% Part 1
dots=[[2,3],[1,5]]
p = Paper(dots)
p.show()
