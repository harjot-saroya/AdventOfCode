import os
f = open(os.getcwd() + "/Desktop/Advent/day3/input.txt", "r")

store = []
for i in f:
    store.append(str(i[:-1]))


def func1():
    location = 0
    trees = 0
    size = len(store[0])
    for line in range(len(store)):

        if location >= len(store[0]):
            location = location % (size)

        if store[line][location] == "#":
            trees += 1
        location += 3
    return trees


# print(func1())


def func2(down, right):
    location = 0
    trees = 0
    size = len(store[0])
    for line in range(0, len(store), down):

        if location >= len(store[0]):
            location = location % (size)

        if store[line][location] == "#":
            trees += 1
        location += right
    return trees


print(func2(1, 1)*func2(1, 3)*func2(1, 5)*func2(1, 7)*func2(2, 1))
