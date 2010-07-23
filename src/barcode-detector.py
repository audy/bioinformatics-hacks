#!/usr/bin/env python
# encoding: utf-8

# for Illumina qseq files
# Count barcodes that are <= 2nt different
# Discard any with '.' or >= 3 in a row.

# Then do the same thing with random sequences, compare.       

from sys import argv
import re
from collections import defaultdict
from random import choice, seed

def score(reads):
    # zero is perfect
    # 7 is opposite of perfect
    score = 0
    for i, j in reads:
        if i == j: score += 1
    return 7 - score

def count(reads, barcodes):
    reggie = re.compile('[G]{3,7}[A]{3,7}[T]{3,7}[C]{3,7}') # <- fugly!!
    counts = defaultdict(int)

    for read in reads:
        if '.' in read: continue
        if reggie.match(read): continue
        #if read in barcodes: counts[read] += 1
        else:
            # super inefficient!
            tries = []
            for code in barcodes:
                if score(zip(code, read)) <= 5:
                    tries.append(code)
                    break
            # Discard if it matches more than one
            #if len(trye) == 1: counts[code] += 1


    for k in counts:
        print '%s => %s' % (k, counts[k])

def random_barcode():
    return ''.join(choice('GATC.') for i in range(7))

def main(argv):
    hq, bc = [ open(f) for f in argv[1:] ]
    reads = ( i.split()[8] for i in hq )
    barcodes = set( [ i.strip() for i in bc  ]  )
    
    print '==> RANDOM <=='
    count((random_barcode() for i in range(124545)), barcodes)
    
    print '==> %s <==' % argv[1]
    count(reads, barcodes)
    

    

if __name__ == '__main__':
    main(argv)