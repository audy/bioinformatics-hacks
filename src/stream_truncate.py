# Truncates a FASTA file input from a stream:

# i.e.
# $ cat felis_catus.fasta | python stream_truncate.py 0 300 > truncated_cat.fa
# ^ This will truncate all records from 0 to 300.

import sys

header = False
sequence = []

beg = int(sys.argv[1])
end = int(sys.argv[2])

for line in sys.stdin:
    if line[0] == '>':
        if header: print header, ''.join(sequence)[beg:end]
        header = line
        sequence = []
    else:
        sequence.append(line.strip())

print header, ''.join(sequence)[beg:end]
