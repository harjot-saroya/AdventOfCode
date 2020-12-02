import os
f = open(os.getcwd()+"/Desktop/Advent/q1-text.txt", "r")
store = {}
for i in f:
    store[int(i)] = 'yerr'


def func1():
    for i in store.keys():
        curr = 2020 - i
        if store.get(curr):
            print(curr * i)
            break


def func2():

    arr = sorted(store.keys())
    for i in range(0, len(arr)-1):
        pivot = arr[i]
        # Remove ith element from array
        rest = arr[:i] + arr[i+1:]
        start = 0
        end = len(rest) - 1
        while start < end:
            # Set sum we want to be 2020 - pivot (ith element)
            find = 2020 - pivot
            # Move start and end pointers accordingly
            if rest[start] + rest[end] == find:
                return rest[start] * arr[i] * rest[end]
            elif rest[start] + rest[end] > find:
                end -= 1
            else:
                start += 1


print(func2())
# func1()
