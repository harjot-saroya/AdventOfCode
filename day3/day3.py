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


# def func2(right_move, down_move):
#     tree_count = 0
#     with open(os.getcwd() + "/Desktop/Advent/day3/input.txt", "r") as f:
#         cursor = 0
#         down_count = 0
#         for line in f:
#             if down_count != 0:
#                 down_count -= 1
#                 continue
#             else:
#                 down_count = down_move - 1
#             # essentially .strip but better complexity
#             line = line[:-1]
#             line_max = len(line)
#             if cursor >= line_max:
#                 index = cursor % line_max
#             else:
#                 index = cursor
#             if line[index] == '#':
#                 tree_count += 1
#             cursor += right_move
#     return tree_count


print(func1())
print(func2(1, 1)*func2(1, 3)*func2(1, 5)*func2(1, 7)*func2(2, 1))
