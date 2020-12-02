import os
f = open(os.getcwd() + "/Desktop/Advent/day2/input.txt", "r")

store = []
for i in f:
    store.append(str(i[:-1]))


def func1():
    # o(n^2)
    valid = []
    for i in store:
        # o(3n) ~ o(n)

        # o(n)
        ind = i.index('-')
        rval = (int(i[:ind]), int(i[ind+1:ind+3]))
        # o(n)
        ind2 = i.index(':')
        char = i[ind2-1]
        word = i[ind2+1:]
        count = 0

        # o(n)
        for x in range(len(word)):
            if count > max(rval):
                break
            if word[x] == char:
                count += 1

        if min(rval) <= count <= max(rval):
            valid.append(word)

    return len(valid)


def func2():
    ret = []

    for i in store:
        ind = i.index('-')
        rval = (int(i[:ind]), int(i[ind+1:ind+3]))
        # o(m)
        ind2 = i.index(':')
        char = i[ind2-1]
        word = i[ind2+1:]

        if (word[min(rval)] == char and word[max(rval)] != char):
            ret.append(word)
        elif (word[min(rval)] != char and word[max(rval)] == char):
            ret.append(word)
        else:
            pass
    return len(ret)


print(func1())
print(func2())
