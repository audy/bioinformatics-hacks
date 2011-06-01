#!/usr/bin/env Python
# Goal: Tooo make a table for training GlimmerHMM using NCBI genome files.
# Austin G. Davis-Richardson
# HareKrishna@Gmail.com

import sys

handles = dict([[fi.split('.')[1], open(fi)] for fi in sys.argv[1:]])
handles['fout'] = open('%s.ffn.out' % fi.split('.')[0], 'w')
handles['tabl'] = open('%s.table' % fi.split('.')[0], 'w')
gfflines = (line.split() for line in handles['gff'].readlines()[4:-1])

for line in gfflines:
    if line[2] == 'gene':
        start = int(line[3])-1
        print >> handles['tabl'], ''
    elif line[2] == 'exon':
        print >> handles['tabl'], 'seq%s %s %s' % \
            (start, int(line[3])-start, int(line[4]) - start)
            
# load entire fasta file, uniqueify and sort

name = None
seqs = {}

for line in handles['ffn']:
    if line[0] == '>':
        if name: seqs[name] = seq
        seq = []
        name = int(line.split(':')[1].split('-')[0].lstrip('c'))-1
    else:
        seq.append(line)
        
for seq in sorted(seqs.keys()):
    print >> handles['fout'], '>seq%s' % seq
    print >> handles['fout'], '%s' % ''.join(seqs[seq]),
            

        
[ handle.close() for handle in handles.values() ]