#!/bin/python3

# Taken from Project Euler: https://projecteuler.net/problem=14
#
#   # Longest Collatz sequence
#
#   The following iterative sequence is defined for the set of positive integers:
#
#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)
#
#   Using the rule above and starting with 13, we generate the following
#   sequence:
#
#       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#   It can be seen that this sequence (starting at 13 and finishing at 1)
#   contains 10 terms. Although it has not been proved yet (Collatz Problem), it
#   is thought that all starting numbers finish at 1.
#
#   Which starting number, under one million, produces the longest chain?
#
#   NOTE: Once the chain starts the terms are allowed to go above one million.

import sys

# calculate a single collatz chain that starts with 'start'
def get_collatz_chain(start):
    chain = []
    chain.append(start)
    while chain[-1] != 1:
        if chain[-1] % 2 == 0:
            chain.append(int(chain[-1] / 2))
        else:
            chain.append(int(3*chain[-1] + 1))
    return chain


try:
    start = int(sys.argv[1])
    single_chain = True
except IndexError:
    single_chain = False

if single_chain:
    print('Calculating collatz chain starting with {}'.format(start))
    my_chain = get_collatz_chain(start)
    print(my_chain)
    print(len(my_chain))

if not single_chain:
    max_chain_length = [0, 0]
    for i in range(1,51):
        chain_i = get_collatz_chain(i)
        if len(chain_i) > max_chain_length[1]:
            max_chain_length[0] = i
            max_chain_length[1] = len(chain_i)
        print('starting at {} leads to chain of length {}'.format(i, len(chain_i)))

    print('longest chain length started at {} and was {} entries ' \
          'long'.format(max_chain_length[0], max_chain_length[1]))
