#!/usr/bin/env bash
for i in {1..24}
do
./nth-permutation.py -p $1 -n $i
done
