# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:06:59 2021

@author: Bouke
"""
import numpy as np

# functies om bingo te spelen
def streepweg(kaart, getal):
    return np.where(kaart == getal, 100, kaart)    

def checkwinst(kaart):
    winst = False # default value
    for n in range(5):
        if sum(list(kaart[n,:])) == 500:
            winst = True
        elif sum(list(kaart[:,n])) == 500:
            winst = True
    return winst
            
#%% part 1
# inlezen kaarten
with open("input-day4.txt", "r") as f:
    input = f.readlines()

trekking = [int(n) for n in input[0].split(',')]
input = input[2:]
bingokaarten = []

for n in range(0, len(input), 6):
    kaart = np.array([[int(i) for i in input[n].split()] for n in range(n, n+5)])
    bingokaarten.append(kaart)

def speelronde(ronde):
    getal = trekking[ronde]
    # voor elke kaart het getrokken getal wegstrepen
    for n in range(100): 
        bingokaarten[n] = streepweg(bingokaarten[n], getal)
    # checken of 1 van deze kaarten gewonnen heeft
    winst = False
    for n in range(100): 
        if checkwinst(bingokaarten[n]):
            calc_ans(bingokaarten[n], getal)
            winst = True
    if not winst:
        speelronde(ronde+1)

# formule voor antwoord part 1
def calc_ans(winnaar, getal):
    print(winnaar)
    resterend = np.where(winnaar == 100, 0, winnaar)
    print('Som van alle resterende getallen is ', sum(sum(resterend)))
    print('dus het antwoord voor dit deel is', sum(sum(resterend))*getal)    

# bingo spelen
speelronde(0)  #uncomment to play again

#%% part 2
def speelronde2(ronde, bingokaarten): #ditmaal elke winnende kaart laten verdwijnen
    getal = trekking[ronde]
    # voor elke kaart het getrokken getal wegstrepen
    if len(bingokaarten) == 1 and checkwinst(bingokaarten[0]):
        calc_ans(bingokaarten[0], trekking[ronde-1])
    elif len(bingokaarten) == 1:
        bingokaarten[0] = streepweg(bingokaarten[0], getal)
        speelronde2(ronde+1, bingokaarten)
    else:
       for n in range(len(bingokaarten)):
            bingokaarten[n] = streepweg(bingokaarten[n], getal)    
       bingokaarten = [kaart for kaart in bingokaarten if not checkwinst(kaart)]
       speelronde2(ronde+1, bingokaarten)

# opnieuw inlezen kaarten
with open("input-day4.txt", "r") as f:
    input = f.readlines()

trekking = [int(n) for n in input[0].split(',')]
input = input[2:]
bingokaarten = []

for n in range(0, len(input), 6):
    kaart = np.array([[int(i) for i in input[n].split()] for n in range(n, n+5)])
    bingokaarten.append(kaart)


# bingo spelen
#speelronde2(0, bingokaarten) #uncomment to play again