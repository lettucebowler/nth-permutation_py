#!/usr/bin/env python3
import argparse
from math import factorial
from copy import deepcopy

def ending(number):
    num_ending = 'th'
    if number == 1:
        num_ending = 'st'
    elif number == 2:
        num_ending = 'nd'
    elif number == 3:
        num_ending = 'rd'
    return num_ending

def last_index_of(a, alphabetical):
    return len(alphabetical) - list(reversed(alphabetical)).index(a)
    

def nth_perm(perm, chars, n, total):
    # if len(perm) < total:
    #     alphabetical = sorted([char for char in chars])
    #     char_frequencies = {i:alphabetical.count(i) for i in alphabetical}
    #     ranges = {a:factorial(len(chars) - 1) * char_frequencies[a] for a in char_frequencies}
    #     for a in ranges:
    #         if n < ranges[a]:
    #             perm.append(a)
    #             chars.remove(a)
    #             break
    #     perm = nth_perm(perm, chars, n, total)
    # else:
    #     print(str(perm))
    #     return list(perm)
    alphabetical = sorted([char for char in chars])
    char_frequencies = {i:alphabetical.count(i) for i in alphabetical}
    multiplier = 1
    for i in char_frequencies:
        multiplier *- char_frequencies[i]:
    ranges = [multiplier * last_index_of(g, alphabetical) for g in char_frequencies]
    while len(perm) < total:



    


# Determine duplicate permutation handlilng based on user preference

    # Determine duplicate multiplier
    # multiplier = 1
    # for letter in duplicates:
    #     multiplier *= factorial(duplicates[letter])
    # n *= multiplier

# q = n - 1
# for x in range(len(alphabetical)):
#     index = q // factorial(len(temp) - 1) % len(temp)
#     nperm.append(temp[index])
#     temp.remove(nperm[-1])

# Parser to get base number for computations
parser = argparse.ArgumentParser(description='Finds the nth permutation of a string \
    when sorted alphabetically')
parser.add_argument('-p', dest='string_to_permute', default='default', required=False)
parser.add_argument('-n', dest='n', default='1', required=False, type=int)
args = parser.parse_args()
initial_permutation = args.string_to_permute
n = args.n

if n > factorial(len(initial_permutation)):
    print("n out of range")
    exit()

# Driver Code
nperm = []
chars = [char for char in initial_permutation]
perm = nth_perm(nperm, chars, n - 1, len(chars))
print('{}{} permutation of {}: {}'.format(str(n), ending(n), initial_permutation, ''.join(perm)))
