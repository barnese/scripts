# Generates a string of random integers.

from __future__ import print_function
import sys
import random
import argparse

# Parse the arguments
parser = argparse.ArgumentParser(prog='genints', description='Generates strings of random integers.', epilog='Example: python genints.py 5 6 1 6')
parser.add_argument('size', type=int, help='the size of each generated number')
parser.add_argument('count', type=int, help='the number of generated numbers')
parser.add_argument('min_int', type=int, help='the min integer to use per number')
parser.add_argument('max_int', type=int, help='the max integer to use per number')
args = parser.parse_args()

size = args.size
count = args.count
min_int = args.min_int
max_int = args.max_int

rand = random.SystemRandom()

for i in range(count):
    for j in range(size):
        print(rand.randint(min_int, max_int), end='')
    print()
