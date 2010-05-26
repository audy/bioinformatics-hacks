#!/usr/bin/env python
import sys

for file in sys.argv[1:]:
    gc = 0
    at = 0

    print '>> %s <<' % file

    with open(file) as handle:
        for line in handle:
            if line[0] == '>':
                continue
            else:
                for char in line:
                    if (char.lower() == 'g') or (char.lower() == 'c'):
                        gc += 1
                    else:
                        at += 1

    print 'gc = %s \nat = %s' % (gc, at)
    print 'gc/tot = %g' % (float(gc)/(gc + at))
