import sys

hclc = open(sys.argv[1])
htxt = open(sys.argv[2])

# Skip 1st line
hclc.next()

getreads = {}

for line in hclc:
    lina = line.lstrip('\"').rstrip('\",\n').split('\",\"')
    reads = lina[2].replace(',','')
    fig, num = lina[4].split('_')
    getreads[(num, fig)] = reads
    
count = 0
    
for line in htxt:
    if line.startswith('Consensus'):
        line = line.strip().split('\t')
        num = line[0][19:]
        line[8] = line[8].strip()
        fig = line[8]
        try:
            line.append(getreads[(num, fig)])
        except KeyError:
            line.append('X')
            count += 1
        
        print '\t'.join(line)
        
print >> sys.stderr, '%s >> skipped: %s' % (sys.argv[2], count)
        
