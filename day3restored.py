# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""

from matplotlib import pyplot as plt

with open("input-day3.txt", "r") as f:
    input = f.readlines()

from statistics import mean

#%% part 1    

bits_per_position = []
for position in range(12):
    bits_list = [number[position] for number in input]
    bits_per_position.append(bits_list)

gamma = ""
epsilon = ""

for bitlist in bits_per_position:
    # oude manier met afronden
    #bitlist = [int(bit) for bit in bitlist]
    #gamma += str(round(mean(bitlist)))
    zerocount = bitlist.count('0')
    onecount = bitlist.count('1')
    if zerocount > onecount:
        gamma += '0'
    elif onecount > zerocount:
        gamma += '1'
    else:
        gamma += '?'
        
# gamma omzetten in epsilon
for bit in gamma:
    if bit == '0':
        epsilon += ('1')
    elif bit == '1':
        epsilon += ('0')
    else:
        print("Error: invalid input")

#binair naar decimaal
gamma_dec = int(gamma, 2) # converteert binair getal str naar decimaal
epsilon_dec = int(epsilon, 2)

print("The answer to part 1 is", gamma_dec*epsilon_dec)
#%% part 2

with open("input-day3.txt", "r") as f:
    input = f.readlines()
# determine the oxgen code:   only keep numbers with values in a certain bit position corresponding to the most common bit value
input_oxgen = input
step=0

while len(input_oxgen) > 1:
#    print("After step", step, "there are" ,len(input_oxgen), "numbers remaining")
    bitlist = [number[step] for number in input_oxgen]
    zerocount = bitlist.count('0')
    onecount = bitlist.count('1')
    if zerocount > onecount:
        most_common = '0'
    elif onecount > zerocount:
        most_common = '1'
    else:
        most_common = '1' # if draw keep the '1' for oxgen
#    print("In step", step, "there are", zerocount, "zeroes, and", onecount, "ones, so", most_common, "prevails") 
    
    input_oxgen = [number for number in input_oxgen if number[step]==most_common]
    step += 1
    if len(input_oxgen) == 1:
        oxgen = input_oxgen[0]
        print("oxygen generator rating is", oxgen)
   
# determine the CO2 scrubber rating:   only keep numbers with values in a certain bit position corresponding to the most common bit value
input_scrubber = input
step=0

while len(input_scrubber) > 1:
#    print("After step", step, "there are",len(input_scrubber), "numbers remaining")
    bitlist = [number[step] for number in input_scrubber]
    zerocount = bitlist.count('0')
    onecount = bitlist.count('1')
    if zerocount < onecount:
        least_common = '0'
    elif onecount < zerocount:
        least_common = '1'
    else:
        least_common = '0' # if draw keep the '1' for oxgen
#    print("In step", step, "there are", zerocount, "zeroes, and", onecount, "ones, so", least_common, "prevails") 
    
    input_scrubber = [number for number in input_scrubber if number[step]==least_common]
    step += 1
    if len(input_scrubber) == 1:
        scrubber = input_scrubber[0]
        print("CO2 scrubber rating is", scrubber)

# construct final answer 
oxgen_dec = int(oxgen, 2) #
scrubber_dec = int(scrubber, 2)

print("The answer to part 2 is", oxgen_dec*scrubber_dec)