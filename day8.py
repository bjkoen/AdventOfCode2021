# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

from matplotlib import pyplot as plt

with open("input-day8.txt", "r") as f:
    input = f.readlines()


#%% part 1    
input1 = [str.split('|')[1].split() for str in input]

input_lengths = []
for line in input1:
    input_lengths.append([len(value) for value in line])

#alles bij elkaar in 1 list
all_lengths = []
for line in input_lengths:
    all_lengths += line
# * = unieke aantallen segmenten per cijfer:
#0:6    #1:2 *   #2:5     #3:5    #4:4 *   #5:5   #6:6   #7:3 *   #8:7 *   #9:6 

# vraag bij part1: hoe vaak komt 1,4,7 of 8 voor

print("The answer to part 1 is", len([value for value in all_lengths if value in [2,4,3,7]]))

#%% part 2
with open("input-day8.txt", "r") as f:
    input = f.readlines()
input = [[str.split('|')[0].split(), str.split('|')[1].split()] for str in input]

def findcode(patterns):
    """Takes a list of the ten observed unique patterns, returns 
    a dictionary of mixed up segment letters corresponding to actual letters"""
    code = {}
    een = next(s for s in patterns if len(s) == 2)
    vier = next(s for s in patterns if len(s) == 4)
    all_segments = ''.join(patterns)
    for letter in 'abcdefg':
        if all_segments.count(letter) == 6:
            code[letter] = 'b'
        elif all_segments.count(letter) == 4:
            code[letter] = 'e'
        elif all_segments.count(letter) == 9:
            code[letter] = 'f'
        elif all_segments.count(letter) == 8:
            if letter in een:
                code[letter] = 'c'
            else:
                code[letter] = 'a'
        elif all_segments.count(letter) == 7:
            if letter in vier:
                code[letter] = 'd'
            else:
                code[letter] = 'g'
        else:
            print('Something went wrong...')     
    return code 

def decode(numbers, code):
    """Takes 2 parameters: a list of four numbers, represented by random segment letters
    and the dictionary created by findcode()
    Returns an integer consisting of the four output digits
    """
    output = "0"
    number_dict = {'abcefg' : '0',
        'cf' : '1',
        'acdeg' : '2',
        'acdfg' : '3',
        'bcdf' : '4',
        'abdfg' : '5',
        'abdefg' : '6',
        'acf' : '7',
        'abcdefg' : '8',
        'abcdfg' : '9'}
    for number in numbers:
        decoded_number = ''.join([code[letter] for letter in number])
        output += number_dict[''.join(sorted(decoded_number))]            
    return int(output)

        
# construct answer:

answer_pt2 = 0    

for line in input:
    code = findcode(line[0])
    answer_pt2 += decode(line[1], code)
    
print('Answer to part 2 is', answer_pt2)
