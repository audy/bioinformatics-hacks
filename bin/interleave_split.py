#!/usr/bin/env python

DESCRIPTION = """

    Splits interleaved fastq files into two separate fastq files
    
    Austin G. Davis-Richardson
    University of Florida
    harekrishna@gmail.com
    http://audy.github.com
    
    Requirements:
     - Tested with Python 2.6, 2.7
     - A UNIX-Like operating system
    
    Usage:
    
     python interleave_split.py filename.fastq > odd.fastq 2> even.fastq
     
    The script prints to STDOUT for odd records and STDERR for even records. 
    I know this is silly, I was trying to be cute. 

"""

import sys
from itertools import cycle
c = cycle(range(1, 9))

with open(sys.argv[1]) as handle:
    for line in handle:
        n = c.next()
        if n < 5:
            print >> sys.stdout, line.strip()
        else:
            print >> sys.stderr, line.strip()
