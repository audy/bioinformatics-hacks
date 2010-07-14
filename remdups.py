# Removes duplicate FASTA records
import sys

seqs = {}
name = None

for line in open(sys.argv[1]):
    if line[0] == '>':
        if name: seqs[name] = seq
        seq = []
        name = line.strip()
    else:
        seq.append(line)
        
for seq in sorted(seqs.keys(), key=):
    print seq
    print ''.join(seqs[seq]),