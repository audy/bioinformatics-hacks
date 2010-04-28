# quick_filter.py - a quick hack by Austin G. Davis-Richardson
# Filters FASTA File by argv[2]
# TODO: Generates Names Hash for ChimeraChecker

import sys
from fastitr import *
from dnaobj import *

def main(argv):

    filename = argv[1]
    keyword = argv[2].lower()
    
    output = open(keyword + '_filtered.txt', 'w')
    
    handle = open(filename, 'r')
    fasta = fastitr(handle, 'fasta')
        
    for record in fasta:
        line = record.header.split()
        acc, name = line[0], ''.join(line[1:])
        names = name.lower().split(';')
        if keyword in names[0]:
            output.write('%s' % record)
            
if __name__ == '__main__':
    main(sys.argv)