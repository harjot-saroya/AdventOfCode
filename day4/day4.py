import os
import re
f = open(os.getcwd() + "/Desktop/Advent/day4/input.txt", "r")


def func1():
    lines = f.readlines()
    curr = {}
    count = 0
    store = []
    # O(n*m)
    for i in lines:
        line = i[:len(i)-1]
        line = line.split(' ')
        for x in line:
            if len(x) != 0:
                curr[str(x[0:3])] = str(x[4:])
            else:
                if (len(curr) >= 7 and curr.get('cid') == None) or (len(curr) == 8):
                    count += 1
                store.append(curr)
                curr = {}
    return count


def func2():
    lines = f.readlines()
    curr = {}
    count = 0
    store = []
    # O(n*m)
    for i in lines:
        line = i[:len(i)-1]
        line = line.split(' ')
        for x in line:
            if len(x) != 0:
                curr[str(x[0:3])] = str(x[4:])
            else:
                if (len(curr) >= 7 and curr.get('cid') == None) or (len(curr) == 8):
                    count += 1
                    store.append(curr)
                curr = {}
    valid = 0
    for x in store:
        check = 'abcdef0123456789'

        byr = 1920 <= int(x.get('byr')) <= 2002
        iyr = 2010 <= int(x.get('iyr')) <= 2020
        eyr = 2020 <= int(x.get('eyr')) <= 2030
        hgt = (x.get('hgt')[len(x.get('hgt')) - 2:] == 'cm' and 150 <= int(x.get('hgt')[:len(x.get('hgt')) - 2]) <= 193) or (
            x.get('hgt')[len(x.get('hgt')) - 2:] == 'in' and 59 <= int(x.get('hgt')[:len(x.get('hgt')) - 2]) <= 76)
        ecl = x.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid = len(x.get('pid')) == 9 and x.get('pid').isdigit()
        charCheck = True
        hcl = x.get('hcl')[0] == '#' and charCheck
        word = x.get('hcl')[1:]
        for i in word:
            if word in check == False:
                charCheck = False
        if byr and iyr and eyr and hgt and ecl and pid and hcl:
            valid += 1
    return valid


print(func2())

#    left = str(x[0:3])
#     right = str(x[4:])
#     if left == 'byr' and 1920 <= int(right) <= 2002:
#         curr[left] = right
#     if left == 'iyr' and 2010 <= int(right) <= 2020:
#         curr[left] = right
#     if left == 'eyr' and 2020 <= int(right) <= 2030:
#         curr[left] = right
#         print(right)
#     if left == 'hgt':
#         if right[len(right) - 2:] == 'cm' and 150 <= int(right[:len(right) - 2]) <= 193:
#             curr[left] = right
#         elif right[len(right) - 2:] == 'in' and 59 <= int(right[:len(right) - 2]) <= 76:
#             curr[left] = right
#     if left == 'ecl' and right in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
#         curr[left] = right
#     if left == 'hcl' and right[0] == '#' and len(right[1:]) == 6:
#         check = 'abcdef0123456789'
#         valid = False
#         for i in right[1:]:
#             if (i in check) == False:
#                 break
#         valid = True
#         if (valid):
#             curr[left] = right

#     if left == 'pid' and right[0] == '0' and len(right) == 9:
#         curr[left] = right
