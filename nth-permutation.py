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
parser.add_argument('-d', action='store_true')
args = parser.parse_args()
initial_permutation = args.string_to_permute
n = args.n
consider_duplicates = args.d

alphabetical = sorted([char for char in initial_permutation])
temp = deepcopy(alphabetical)
nperm = []

# Determine duplicate permutation handlilng based on user preference
if consider_duplicates:
    # Determine duplicate multiplier
    duplicates = {i:alphabetical.count(i) for i in alphabetical}
    multiplier = 1
    for letter in duplicates:
        multiplier *= factorial(duplicates[letter])
    n *= multiplier

q = n - 1
for x in range(len(alphabetical)):
    index = q // factorial(len(temp) - 1) % len(temp)
    nperm.append(temp[index])
    temp.remove(nperm[-1])

print(str(n) + '{} permutation of {}: '.format(ending(n), initial_permutation) + ''.join(nperm))