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

def get_range(alphabetical, c, fact):
    index = len(alphabetical) - list(reversed(alphabetical)).index(c)
    range = index * factorial(len(alphabetical) - 1)
    return range
    

def nth_perm(perm, chars, n):
    alphabetical = sorted([char for char in initial_permutation])
    char_frequencies = {i:alphabetical.count(i) for i in alphabetical}
    counts = [factorial(len(chars) - 1) * char_frequencies[a] for a in char_frequencies]
    # fact = factorial(len(chars))
    # nperm = []
    # for i in range(len(chars)):
    #     # Find frequency of each letter    
    #     alphabetical = sorted([char for char in initial_permutation])
    #     for use in nperm:
    #         alphabetical.remove(use)
    #     print('{}'.format(alphabetical))
    #     char_frequencies = {i:alphabetical.count(i) for i in alphabetical}
    #     for i, char in enumerate(sorted(list(set(alphabetical)))):
    #         # print('{}:{}'.format(i, char))
    #         r = get_range(alphabetical, char, fact)
    #         print('{}'.format(r))
    #         if n < r:
    #             nperm.append(char)
    #             break
    return perm


    


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
perm = nth_perm(nperm, initial_permutation, n - 1)
print('{}{} permutation of {}: {}'.format(str(n), ending(n), initial_permutation, ''.join(perm)))
