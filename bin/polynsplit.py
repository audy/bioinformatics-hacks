#!/usr/bin/env python
# encoding: utf-8

# Splits a single fasta record into a multifasta when a string of 10 or more Ns is encountered.

import re
import sys

reggie = re.compile('[N]{10}[N]*') # match 10 or more Ns


count = 0
sequence = []
 
with open(sys.argv[1]) as handle:
    for line in handle:
        if line.startswith('>'):
            title = line[1:-1]
        else:
            sequence.append(line.strip())

sequence = ''.join(sequence)

sequence = re.split('[N]{10}[N]*', sequence)

for seq in sequence:
    count += 1
    print '>%s %s\n%s\n' % (title, count, seq)
