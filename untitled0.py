# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:24:42 2020

@author: kreoc
"""

import itertools
import numpy as np
import random

"""
# all 15 cubes

number = [1,2,3,4,5,6]
results = itertools.combinations(number,4)
all = list(results)
print(all)
#print(len(all))
"""


# core

arr = np.arange(1,7)
np.random.shuffle(arr)
print(arr)
two_more = np.random.choice(arr[:4], 2, replace=False)
print(two_more)
core = np.append(arr,two_more) 
print(core) 

# grid zeros

s = (15,4)
grid = np.zeros(s)
#print(grid)
print(grid[2])


# start grid
def start_grid():
    grid[6] = [core[0], core[1], core[2], core[3]]
    grid[7] = [core[2], core[3], core[4], core[5]]
    grid[8] = [core[4], core[5], core[6], core[7]]

    grid[0] = [0, 0, 0, core[0]]
    grid[1] = [0, core[0], 0, core[2]]
    grid[2] = [0, core[2], 0, core[4]]
    grid[3] = [0, core[4], 0, core[6]]
    grid[4] = [0, core[6], 0, 0]
    grid[5] = [0, 0, core[0], core[1]]
    grid[9] = [core[6], core[7], 0, 0]
    grid[10] = [0, 0, core[1], 0]
    grid[11] = [core[1], 0, core[3], 0]
    grid[12] = [core[3], 0, core[5], 0]
    grid[13] = [core[5], 0, core[7], 0]
    grid[14] = [core[7], 0, 0, 0]
    return grid

#print(grid)


# border
def border_search(grid):
    
    grid[1][2] = random.choice([x for x in range(1,7) if x != core[0] and x != core[2] and x!= core[4]]) #b
    grid[2][0] = grid[1][2]
    
    grid[2][2] = random.choice([x for x in range(1,7) if x != core[2] and x != core[4] and x!= core[6] and x != grid[1][2]]) #c
    grid[3][0] = grid[2][2]
    
    grid[3][2] = random.choice([x for x in range(1,7) if x != core[4] and x!= core[6] and x != grid[2][2]]) #d
    grid[4][0] = grid[3][2]
    
    grid[4][3] = random.choice([x for x in range(1,7) if x != core[6] and x != core[7] and x != grid[3][2]]) #e
    grid[9][2] = grid[4][3]
    
    grid[9][3] = random.choice([x for x in range(1,7) if x != core[6] and x != core[7] and x != grid[4][3]]) #f
    grid[14][2] = grid[9][3]
    
    grid[14][1] = random.choice([x for x in range(1,7) if x != core[7] and x != core[5] and x != grid[9][3]]) #g
    grid[13][3] = grid[14][1]
    
    grid[13][1] = random.choice([x for x in range(1,7) if x != core[7] and x != core[5] and x != core[3] and x != grid[14][1]]) #h
    grid[12][3] = grid[13][1]
    
    grid[12][1] = random.choice([x for x in range(1,7) if x != core[1] and x != core[3] and x != core[5] and x != grid[13][1]]) #i
    grid[11][3] = grid[12][1]
    
    grid[11][1] = random.choice([x for x in range(1,7) if x != core[1] and x != core[3] and x != grid[12][1]]) #j
    grid[10][3] = grid[11][1]
    
    grid[10][0] = random.choice([x for x in range(1,7) if x != core[0] and x != core[1] and x != grid[11][1]]) #k
    grid[5][1] = grid[10][0]
    
    grid[5][0] = random.choice([x for x in range(1,7) if x != core[0] and x != core[1] and x != grid[10][0]]) #l
    grid[0][1] = grid[5][0]
    
    grid[0][2] = random.choice([x for x in range(1,7) if x != core[0] and x != core[2] and x != grid[1][2] and x != grid[5][0]]) #a
    grid[1][0] = grid[0][2]
    
    
    grid[0][0] = random.choice([x for x in range(1,7) if x != core[0] and x != grid[0][2] and x != grid[5][0]]) #m
    grid[4][2] = random.choice([x for x in range(1,7) if x != core[6] and x != grid[3][2] and x != grid[4][3]]) #n
    grid[14][3] = random.choice([x for x in range(1,7) if x != core[7] and x != grid[14][1] and x != grid[9][3]]) #o
    grid[10][1] = random.choice([x for x in range(1,7) if x != core[1] and x != grid[10][0] and x != grid[11][1]]) #p
    
    return grid


def compare(s, t):
    return sorted(s) == sorted(t)

def border_control(grid):
    check = []
    for i in range(len(grid)):
        for j in range(i+1,len(grid)):
            check.append(compare(grid[i],grid[j]))
    print(check)
    return (check)


b = border_search(grid)
A = True
while A:
    if any(border_control(b)):
        b = border_search(grid)
    else:
        A = False
        print(grid)

