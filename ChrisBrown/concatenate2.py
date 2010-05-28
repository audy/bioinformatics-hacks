#!/usr/bin/env python
import os
import sys

for file in os.listdir(sys.argv[1]):
    if '.txt' in file:
        name = file.rstrip('.txt')
        handle = open('%s/%s' % (sys.argv[1], file))
        for line in handle:
            if line.startswith('Consensus'):
                print '%s\t%s' % (line.strip(), name)
