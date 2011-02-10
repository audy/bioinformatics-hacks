#!/usr/bin/env ython

import sys

with open(sys.argv[1]) as handle:
    for line in handle:
        if line.startswith('>'):
            keep = False
            if sys.argv[2] in line.lower():
                keep = True
                print line.strip()
        else:
            if keep:
                print line.strip()
