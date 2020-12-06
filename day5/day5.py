import os
import math
f = open(os.getcwd() + "/Desktop/Advent/day5/input.txt", "r")

lines = f.readlines()

# 0-127
# F is lower half
# B is upper half
# 0-7
# R is upper half
# L is lower half


def func1():
    currmax = float('-inf')
    for line in lines:
        pos = [0, 127]
        pos2 = [0, 7]
        for i in line:
            if i == 'F':
                move = math.floor((pos[1]-pos[0]) / 2)
                pos = [pos[0], pos[0]+move]
            elif i == 'B':
                move = math.ceil((pos[1]-pos[0]) / 2)
                pos = [move+pos[0], pos[1]]
            elif i == 'L':
                move = math.floor((pos2[1]-pos2[0]) / 2)
                pos2 = [pos2[0], pos2[0]+move]
            elif i == 'R':
                move = math.ceil((pos2[1]-pos2[0]) / 2)
                pos2 = [move+pos2[0], pos2[1]]
        res = pos[0]
        res2 = pos2[0]
        seat = res * 8 + res2
        currmax = max(currmax, seat)
    return currmax


def func2():
    seats = []

    for line in lines:
        pos = [0, 127]
        pos2 = [0, 7]
        for i in line:
            if i == 'F':
                move = math.floor((pos[1]-pos[0]) / 2)
                pos = [pos[0], pos[0]+move]
            elif i == 'B':
                move = math.ceil((pos[1]-pos[0]) / 2)
                pos = [move+pos[0], pos[1]]
            elif i == 'L':
                move = math.floor((pos2[1]-pos2[0]) / 2)
                pos2 = [pos2[0], pos2[0]+move]
            elif i == 'R':
                move = math.ceil((pos2[1]-pos2[0]) / 2)
                pos2 = [move+pos2[0], pos2[1]]
        res = pos[0]
        res2 = pos2[0]
        seat = res * 8 + res2
        seats.append(seat)

    seats = sorted(seats)

    missing = []
    for i in range(len(seats[1:-1])):
        if (seats[i-1] == seats[i]-1 and seats[i+1] == seats[i]+1) == False:
            missing.append(seats[i])

    return missing


print(func1())
print(func2())
