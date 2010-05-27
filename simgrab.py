# simgrab.py

# Austin G. Davis-Richardson
# Two fasta files
# Scripts takes header from one, gets corresponding sequence from two
# Prints out two

import sys


# first argument is query
# second argument is database

query = []

with open(sys.argv[1]) as handle:
    for line in handle:
        if line[0] == '>':
            query.append(line.strip())

query = set(query)

print_seq = False

with open(sys.argv[2]) as handle:
    for line in handle:
        if line[0] == '>':
            if line.strip() in query:
                print_seq = True
                print line
            else:
                print_seq = False
        elif print_seq:
            print line
