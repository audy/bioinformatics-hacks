from fasta import *
import sys

with open(sys.argv[1]) as handle:
    for record in Fasta(handle, filetype="fasta"):
        for word in ' '.join(sys.argv[2:]).strip('\"').split(', '):
            if word in record.header:
                record.sequence[-1] = record.sequence[-1].strip()
                print '%s' % record,