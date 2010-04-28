# Austin G. Davis-Richardson
# harekrishna@gmail.com

# SHORT:     Prints a truncated version of the input FASTA file.
# USAGE:     Python truncater.py fasta_file start end > outputfile
# NOTE:      First nucleotide is 0, not 1.
# ALSO:      There are no precuations implemented in case the truncation
#            overruns the length of the sequence.  The script will crash.
#            So don't try to truncate anything shorter than your range.

# Requires fastitr and dnaobj by me.
# Works on FASTA alignments, too.

from fastitr import *
from dnaobj import *
import sys

def main(argv):
    
    filename, start, end = argv[1:]
    start, end = int(start), int(end)
    
    handle = open(filename, 'r')

    fasta = fastitr(handle, 'fasta')

    for record in fasta:
        truncated_sequence = do_the_truncation(record, start, end)
        record.sequence = truncated_sequence
        print '%s' % record
        
        
def do_the_truncation(record, start, end):
    return '%s' % record.sequence[start:end]

if __name__ == '__main__':
    main(sys.argv)