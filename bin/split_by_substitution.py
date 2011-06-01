#!/usr/bin/env python

import sys
from collections import defaultdict

'''
Split By Substitution

Austin G. Davis-Richardson

CLC Genomics Workbench can generate a
SNP table from a reference assembly.
Someone asked me to split this table
up by the nature of the SNP.

I thought my solution was clever :)

'''

categories = {
    'nonpolar-hydrophobic': ('Ala', 'Val', 'Leu', 'Ile', 'Phe', 'Trp', 'Met', 'Pro'),
    'polar-uncharged': ('Gly', 'Ser', 'Thr', 'Cys', 'Tyr', 'Asn', 'Gln'),
    'polar-acidic': ('Asp', 'Glu'),
    'polar-basic': ('Lys', 'Arg', 'His'),
    'aromatic': ('Phe', 'Trp', 'Tyr', 'His'),
    'stop': ('Stp',),
}

groupings = defaultdict(set)

for category in categories:
    amino_acids = categories[category]
    for amino_acid in amino_acids:  
        groupings[amino_acid].add(category)
        

with open(sys.argv[1]) as csv_file:
    csv_file.next()
    for line in csv_file:
        substitution = line.split(',')[-1].strip()
        start = substitution[:3]
        end = substitution[-3:]
        mutation = '%s_to_%s' % (' '.join(groupings[start]), ' '.join(groupings[end]))
        with open('output/%s.csv' % mutation, 'a') as output:
            print >> output, line.strip()