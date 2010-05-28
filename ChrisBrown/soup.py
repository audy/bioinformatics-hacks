import sys
import os

from collections import defaultdict

path = sys.argv[1]
files = sorted(os.listdir(path))
for file in files:
    if file.startswith('.'):
        del file

shortnames = [ i.split('.')[0] for i in files ]

names = defaultdict(dict)

print 'name\tcategory\t%s' % '\t'.join(shortnames)

for file in files:
    if not file.endswith('.txt'):
        continue
    handle = open(path + file, 'r')
    for line in handle:
        line = line.strip().split('\t')
        name, reads, type =  line[7], line[10], line[9]
        if reads == 'X':
            reads = 0
        reads = int(reads)
            
        try:
            names[name][file.split('.')[0]]['reads'] += reads
        except:
            names[name][file.split('.')[0]] = reads
            names[name]['type'] = type
            

for name in names:
    print '%s\t%s\t' % (name, names[name]['type']),
    for file in shortnames:
        try:
            print '%s\t' % (names[name][file]),
        except:
            print '0\t',
    print '\n',
    
