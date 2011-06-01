# interleaves two fasta files (assumes they're congruent)
# Also, assumes sequences are on one line
# Uses headers from first file

import sys
from itertools import izip

handle1 = open(sys.argv[1], 'r')
handle2 = open(sys.argv[2], 'r')

for line1, line2 in izip(handle1, handle2):
    if line1[0] == '>':
        print line1.strip()
    else:
        print line1.strip() + line2.strip()
