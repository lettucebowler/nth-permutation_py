#!/usr/bin/env python3
import argparse
from math import factorial

# Parser to get base number for computations
parser = argparse.ArgumentParser(description='Finds the nth permutation of a string \
    when sorted alphabetically')
parser.add_argument('-p', dest='string_to_permute', default='example', required=False)
args = parser.parse_args()
initial_permutation = args.string_to_permute

start = [char for char in initial_permutation]