#!/usr/bin/env python

#Gets random fastas given a probability

import sys
from fasta import *

filename, probability = sys.argv[1], sys.argv[2]

yes = int(probability.split('/')[0])
no = int(probability.split('/')[1])
yes = yes*[True]
no = no*[False]

yesno = yes + no
import random

random.seed()

with open(filename) as handle:
    records = Fasta(handle, 'fasta')
    for record in records:
        if random.choice(yesno):
            print record