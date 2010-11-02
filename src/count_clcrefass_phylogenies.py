#!/usr/bin/env python
# Austin G. Davis-Richardson

# CLC Ref Assembly + RDP => Description, number of reads

# How to:

# Python <1, 0 or 10> <fasta> <clc table>
# 1  = paired
# 0  = not paired
# 10 = both

''' 
  Print information about each match in an assembly file. The columns are:

    0 Read number
    1 Read name (enable using the `-n' option)
    2 Read length
    3 Read position for alignment start
    4 Read position for alignment end
    5 Reference sequence number
    6 Reference position for alignment start
    7 Reference position for alignment end
    8 Whether the read is reversed (0 = no, 1 = yes)
    9 Number of matches
    10 Whether the read is paired with the next one (0 = no, 1 = yes) (enable
                                                          using the `-p' option
    11 Alignment score (enable using the `-s' option)

'''
import sys
from collections import defaultdict

paired = defaultdict(int)
unpaired = defaultdict(dict)

f_rdp, f_db = sys.argv[1:]

with open(f_db) as handle:
    for line in handle:
        line = line.split()
    
        if line[10] is '1': # then it's paired
            paired[int(line[5])] += 1
            try:
                handle.next() # dont count twice, skip next line
            except StopIteration:
                continue
        elif line[10] is '0': # then it's not paired
            current = int(line[5])
            try:
                next = int(handle.next().split()[5])
                if next in unpaired[current]:
                    unpaired[current][next] += 1
                else:
                    unpaired[current][next] = 1
            except StopIteration:
                continue

# load RDP; we need random access!
rdp, c = {}, 0
with open(f_rdp) as handle:
    for line in handle:
        if line.startswith('>'):
            c += 1
            rdp[c] = line[1:-1]


merged_counts = defaultdict(int) # getting uglier

for first in unpaired:
    for second in unpaired[first]:
        try:
            first_name = rdp[first]
            second_name = rdp[second]
        except KeyError:
            continue
            
        first_name = first_name.split(';')
        second_name = second_name.split(';')
        consensus = []
        for f, s in zip(first_name, second_name):
            if f == s:
                consensus.append(f)
            else:
                merged_counts[';'.join(consensus)] = unpaired[first][second]
                break
                 
with open('%s.unpaired.out' % sys.argv[2], 'w') as handle:
    for c in merged_counts:
        print >> handle, '%s, %s' % (c, merged_counts[c])
    
with open('%s.paired.out' % sys.argv[2], 'w') as handle:
    for hit in paired:
        print >> handle, '%s, %s' % (rdp[hit], paired[hit])
    
        