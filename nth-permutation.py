#!/usr/bin/env python3
import argparse
from math import factorial
from copy import deepcopy

# Parser to get base number for computations
parser = argparse.ArgumentParser(description='Finds the nth permutation of a string \
    when sorted alphabetically')
parser.add_argument('-p', dest='string_to_permute', default='default', required=False)
parser.add_argument('-n', dest='n', default='1', required=False, type=int)

args = parser.parse_args()
initial_permutation = args.string_to_permute
n = args.n

alphabetical = sorted([char for char in initial_permutation])
temp = deepcopy(alphabetical)
nperm = []

q = n - 1
for x in range(len(alphabetical)):
    index = q // factorial(len(temp) - 1) % len(temp)
    nperm.append(temp[index])
    temp.remove(temp[index])

print(str(n) + 'th permutation: ' + ''.join(nperm))