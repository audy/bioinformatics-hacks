DESCRIPTION = ''' 
Duplicate filtering for FASTQ/FASTA data.

If there are at least N duplicates in X basepairs, discard the read (in both pairs).

usage python filter.py <sequences> <N> <X>
'''
import sys
from itertools import izip
from collections import defaultdict
import string
_complement = string.maketrans('GATCRYgatcry','CTAGYRctagyr')

def duplicate_filter(*args, **kwargs):
    ''' removes sequences that have duplicates
from paired-end illumina data '''

    hashes = defaultdict(int)
    count = 0 
    county = 0
    
    filename = kwargs['filename']
    
    with open(filename) as handle:
        for record in Fasta(handle, filetype='fasta'):
            county += 1
            if record.seq in hashes:
                # do not print
                count += 1
                continue
            else:
                print record
                hashes[record.seq] = 1
            
    print >> sys.stderr, 'removed %s out of %s records' % (count, county)


class Fasta:
    ''' iterates through a fastq file, returning dnaobj objects '''
    def __init__(self, *args, **kwargs):
        try:
            self.filetype = kwargs['filetype']
        except KeyError:
            raise Exception, 'use: Fasta(handle, filetype=\'fastq or fastq\')'
        self.handle = args[0]
        self.county = 0
    def __iter__(self):
        if self.filetype == 'fastq':
            counter = 0
            rec = { 0: '', 1: '', 2: '', 3: '' }
            for line in self.handle:
                if line.strip() == '': continue
                if counter < 3:
                    rec[counter] = line.strip()
                    counter += 1
                elif counter == 3:
                    rec[counter] = line.strip()
                    counter = 0
                    yield Dna(rec[0], rec[1], rec[3])
        elif self.filetype == 'fasta':
            header, sequence = '', []
            for line in self.handle:
                if line[0] == '>':
                    if sequence: yield Dna(header, '\n'.join(sequence))
                    header = line
                    sequence = []
                else:
                    sequence.append(line.strip())
            yield Dna(header, '\n'.join(sequence))
            
            
class Dna:
    ''' An object representing either a FASTA or FASTQ record '''
    def __init__(self, header, sequence, quality = False):
        self.header = header[1:-1]
        self.seq = sequence
        self.qual = quality
        if quality:
            self.type = 'fastq'
        else:
            self.type = 'fasta'
        if self.type == 'fastq' and len(self.seq) != len(self.qual):
            raise IOError, \
                'Seq length and qual length do not agree: %s' % (self.header)
    def __str__(self):
        ''' returns a FASTA/Q formatted string '''
        if not self.qual:
            return ('>%s\n%s') % \
                (self.header, self.seq)
        else:
            return('@%s\n%s\n+%s\n%s') % \
                (self.header, self.seq, self.header, self.qual)
    def __len__(self):
        return len(''.join(self.seq))
    def __repr__(self):
        return '<dnaobj.%s instance: %s>' % (self.type, self.header)
    @property
    def complement(self):
        ''' returns complement of sequence '''
        return self.seq.translate(_complement)
    @property 
    def revcomp(self):
        ''' returns reverse complement of sequence '''
        return self.complement[::-1]
    @property
    def rqual(self):
        ''' returns reverse quality'''
        return self.qual[::-1]    
    
if __name__ == '__main__':
    from sys import argv
    filename = argv[1]
    duplicate_filter(filename=filename)
