# Austin Davis-Richardson
# harekrishna@gmail.com

# silva_filter.py
# Removes sequences with ambiguous nucleotides and converts from RNA to DNA

from fastitr import *
import string
import sys

def main(argv):
    non_ambiguous_nucleotides = (' ', '\n', '.', '-', 'A', 'T', 'G', 'U', 'C')
    translation_table = string.maketrans('.-GAUC','.-CTAG')
    
    filename = argv[1]
    handle = open(filename, 'r')
    fasta = fastitr(handle, 'fasta')
    
    for record in fasta:
        print_me = True
        for char in record.sequence.upper().strip():
            if char not in non_ambiguous_nucleotides:
                print_me = False
                break
                
        if print_me:
            record.sequence = string.translate(record.sequence.upper(), translation_table)
            print '%s' % record 

if __name__ == '__main__':
    main(sys.argv)