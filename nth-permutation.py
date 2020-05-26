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
alphabetical = sorted([char for char in initial_permutation])
temp = deepcopy(alphabetical)
nperm = []

# Determine duplicate multiplier
char_frequencies = {i:alphabetical.count(i) for i in alphabetical}
multiplier = 1
for letter in char_frequencies:
    multiplier *= factorial(char_frequencies[letter])
if multiplier != 1:
    print('This program cannot yet handle duplicates in the input string')
    exit()

# Generate nth-permutation
q = n - 1
for x in range(len(alphabetical)):
    index = q // factorial(len(temp) - 1) % len(temp)
    nperm.append(temp[index])
    temp.remove(nperm[-1])

print('{}{} permutation of {}: {}'.format(str(n), ending(n), initial_permutation, ''.join(nperm)))