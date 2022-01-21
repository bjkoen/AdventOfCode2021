# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 12:03:47 2021

@author: Bouke
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from IPython.display import clear_output
from time import sleep
with open("input-day11.txt", "r") as f:
    input = f.readlines()

# input = ['5483143223', # example input
# '2745854711',
# '5264556173',
# '6141336146',
# '6357385478',
# '4167524645',
# '2176841721',
# '6882881134',
# '4846848554',
# '5283751526']

input = np.array([[int(letter) for letter in line.strip()] for line in input])

class Octopuses:
  def __init__(self, array, final_step):
    self.array = array.copy()
    self.step = 0
    self.totalflashes = 0
    self.flashed_this_step = []
    self.final_step = final_step
  
  def new_step(self):
    if self.step > self.final_step: # om te stoppen na stap 100, antwoord deel 1
      pass
    elif len(self.flashed_this_step) == 100: # om te stoppen als alle octopussen in sync zijn
      pass
    else:
      for octopus in self.flashed_this_step: self.array[octopus] = 0
      self.step += 1
      self.totalflashes += len(self.flashed_this_step)
      self.flashed_this_step = []
      self.show()
      self.array += 1
      self.flash()
    
  def flash(self):
    new_flash = False # boolean indicating if any new octopus flashed this iteration
    for index, octopus in np.ndenumerate(self.array):
      if octopus > 9 and index not in self.flashed_this_step:
        self.flashed_this_step.append(index)
        new_flash = True
        neighbours = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for neighbour in neighbours:
          nindex = (index[0]+neighbour[0], index[1]+neighbour[1])
          if 0 <= nindex[0] <= 9 and 0 <= nindex[1] <= 9:
            self.array[nindex] += 1
    self.show()
    if new_flash: # if new flashes occurred during this flash step, try again
      self.flash()
    else:          # if no new flashes occurred, we move on to the next step
      self.new_step()
  
  def show(self):
    plt.figure()
    plt.grid(False)
    plt.title('Step: '+str(self.step)+'  total flashes:'+str(self.totalflashes))
    plt.imshow(self.array, interpolation='nearest', cmap='Greys_r', vmin=0, vmax=10, origin='upper')
    for x,y in self.flashed_this_step:
      plt.plot(x,y,'+r')
    plt.show()
    clear_output(wait=True)
    sleep(0.1)
    
sea = Octopuses(input, 1000)
sea.new_step()