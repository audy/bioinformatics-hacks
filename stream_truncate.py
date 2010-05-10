import sys

header = ''
sequence = []

beg = int(sys.argv[1])
end = int(sys.argv[2])

for line in sys.stdin:
    if line[0] == '>':
        print header, ''.join(sequence)[beg:end]
        header = line
        sequence = []
    else:
        sequence.append(line.strip())
