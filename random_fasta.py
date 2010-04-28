## Austin G. Davis-Richardson
## harekrishna@gmail.com

## Chim_gen.py - Outputs records randomly from an input FASTA file

## USAGE: python chim_gen.py infile.fa number_of_randoms > output.fa

## NOTE:  You must have enough RAM to hold the FASTA file as this
##        script requires random-access

## Headers should look like this >ACCESSION_description
## They'll end up looking like >Accession#1_Accession_#2_Breakpoint

import sys
import random

class dna:
    ''' Object representing a FASTA record. '''
    def __init__(self, header, sequence):
        self.head = header
        self.seq = sequence
    def __repr__(self):
        return '<DNA: %s >' % (self.head)
    def __str__(self, separator=''):
        return '>%s\n%s' % (self.head, separator.join(self.seq))
    def __len__(self):
        return len(''.join(self.seq))
    def sequence(self, separator=''):
        return separator.join(self.seq)
        
class fasta:
    ''' A FASTA iterator/generates DNA objects. '''
    def __init__(self, handle):
        self.handle = handle
    def __iter__(self):
        header, sequence = '', []
        for line in self.handle:
            if line[0] == '>':
                if sequence: yield dna(header, sequence)
                header = line[1:].strip()
                sequence = []
            else:
                sequence.append(line.strip())
        yield dna(header, sequence)

def main(argv):
    """docstring for main"""
    
    handle = open(argv[1])
    howmany = int(argv[2])
    records = [ record for record in fasta(handle) ]
    
    length = len(records)
    
    for i in range(0, howmany):
        random_record = records[random.randint(0, length)]
      
        print random_record
        
        
        
if __name__ == '__main__':
    main(sys.argv)