'''
dnaobj.py

An object representing a FASTA or FASTQ record.

Austin Glenn Davis-Richardson
austingdr@gmail.com
Triplett Lab, University of Florida
'''

import string

_complement = string.maketrans('GATCRYgatcry','CTAGYRctagyr')

class dnaobj:
    ''' An object representing either a FASTA or FASTQ record '''
    def __init__(self, header, sequence, quality = False):
    
        self.header = header[1:]
        self.sequence = sequence
        self.quality = quality
        
        if quality:
            self.type = 'fastq'
        else:
            self.type = 'fasta'
    
    def __str__(self):
        ''' returns a FASTA/Q formatted string '''
        if not self.quality:
            return ('>%s\n%s\n') % (self.header, self.sequence)
        else:
            return('@%s\n%s\n+%s\n%s\n') % (self.header, self.sequence, self.header, self.quality)
            
    def __repr__(self):
        return '<dnaobj.%s instance: %s>' % (self.type, self.header)
            
    def complement(self):
        ''' returns complement of sequence '''
        return self.sequence.translate(_complement)
            
    def revcomplement(self):
        ''' returns reverse complement of sequence '''
        return self.complement()[::-1]
        
    def sequence(self):
        ''' returns DNA sequence '''
        return self.sequence
        
    def quality(self):
        ''' returns quality '''
        return self.quality
        
    def nucqual(self):
        ''' returns ('sequence', 'quality') '''
        return self.sequence, self.quality
