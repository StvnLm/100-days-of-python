'''
Question:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
'''

import time

# With while loop
t1 = time.time()
time.sleep(1)

def solve(heads, legs):
    chickens, rabbits = 0, 0
    rabbits =  heads
    while (((rabbits * 4) + (chickens * 2)) != legs) or (rabbits + chickens) != heads:
        rabbits -= 1
        chickens += 1
    print(f'chickens: {chickens}, rabbits: {rabbits}')
solve(35, 94)

t2 = time.time()
print('while', t2 - t1)


# With for loop
t3 = time.time()
time.sleep(1)

def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)

t4 = time.time()
print('for', t4 - t3)
