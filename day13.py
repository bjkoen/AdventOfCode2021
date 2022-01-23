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

#%% initiating Paper class and defining functions
class Paper:
  def __init__(self, dots): # initialize paper from list of (x,y) coordinates of dots
    xmax,ymax = max([dot[0] for dot in dots]), max([dot[1] for dot in dots])
    self.gridsize = (xmax+1, ymax+1)
    self.array = np.zeros(self.gridsize)
    for x,y in dots:
      self.array[x,y] = 1
    self.array = self.array.transpose()
       
  def show(self, c='blue'): # plot the current dots on the plot
    x,y = np.where(self.array >= 1)[0], np.where(self.array>= 1)[1]
    fig, ax=plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xlim(-1, self.gridsize[0]+1)
    ax.set_ylim(-1, self.gridsize[1]+1)
    ax.scatter(x,y, marker=".", c=c)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.axhline(y=5, c='red')
    fig.show()

  def fold(self, fold):
    self.free_flap = self.array[:,fold+1:].copy()
    self.fixed_flap = self.array[:,:fold].copy()
    print('fixed', self.fixed_flap.shape)
    print('free', self.free_flap.shape)
    self.flipped_free_flap = np.flipud(self.free_flap)
    self.array = self.fixed_flap + self.flipped_free_flap
    
        

#%%%%% Part 1
dots=[(2,7),(5,10)]
p = Paper(dots)
p.show()
p.fold(5)
p.show()
