# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

with open("input-day6.txt", "r") as f:
    input = f.readlines()
input = [int(n) for n in input[0].split(',')]

#%% Test data part1    

testdata = [3,4,3,1,2]

def spawn(currentgen, gen_number):
    nextgen = []
    babies = 0
    gen_number += 1
    
#    print(gen_number) #uncomment als je progress wil checken
    for fish in currentgen:
        if fish == 0:
            nextgen.append(6)
            babies += 1
        else:
            nextgen.append(fish-1)
    
    nextgen += [8 for n in range(babies)]
    
    if gen_number == 80:
        print("Answer is", len(nextgen))
    
    if gen_number < 81:
        spawn(nextgen, gen_number)
 
print("Answer testdata:")
spawn(testdata, 0)
#%% part 1

print("Answer part 1:")
spawn(input,0)

#%% part 2

with open("input-day6.txt", "r") as f:
    input = f.readlines()
input = [int(n) for n in input[0].split(',')]


firstgen = [input.count(n) for n in range(9)]

def visualize(x, y):
    from matplotlib import pyplot as plt
    x = x; y = y
    plt.plot(x,y)
    plt.yscale('log')

def spawn2(currentgen, gen_number, tracker):
#    print(gen_number, currentgen)
    nextgen = [0 for i in range(9)]
    for n in range(1,9):
        nextgen[n-1] = currentgen[n]
    nextgen[8] = currentgen[0]
    nextgen[6] += currentgen[0]
    
    gen_number += 1
    tracker.append(sum(nextgen))
        
    if gen_number == 256:
        print("Answer is", sum(nextgen))
        visualize(list(range(gen_number+1)), tracker)
    if gen_number < 257:
        spawn2(nextgen, gen_number, tracker)

spawn2(firstgen, 0, [sum(firstgen)])