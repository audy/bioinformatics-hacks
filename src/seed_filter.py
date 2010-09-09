#!/usr/bin/env Python
# encoding: utf-8

from fasta import *
import sys

filename = sys.argv[1]
prefix = filename.split('.')[0]

h_ss = open(prefix + '_ss.fa', 'w')
h_bo = open(prefix + '_bo.fa', 'w')

c_ss, c_gi, c_bo, c_un = 0, 0, 0, 0
total = 0 

with open(sys.argv[1]) as handle:
    records = Fasta(handle, 'fasta')
    for record in records:
        record.header = record.header.replace('\t', '')
        total += 1
        if 'unknown' in record.header:
            c_un += 1
            continue
        elif 'SS' in record.header:
            print >> h_ss, '%s' % record,
            c_ss += 1
        else:
            print >> h_bo, '%s' % record,
            c_bo += 1
            continue
            
print 'unknown  = %s' % c_un
print 'just SS  = %s' % c_ss
print 'all else = %s' % c_bo