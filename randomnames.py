# Takes input fastq file, outputs fastq file with random unique headers
# Wrote this to get around CLC Genomics Workbench naming all sequences 
# "No Name"

# Uses Markov Models to generate names!

# Austin G. Davis-Richardson

from fasta import *
from sys import argv as argh
from random import randint as randy

def main(argh):

    filename = argh[1]
    handle = open(filename)

    
    for record in Fasta(handle, 'fastq'):
        name = randy(0, 18446744073709552000)
        record.header = name
        print '%s' % record,
    

if __name__ == '__main__':
    main(argh)