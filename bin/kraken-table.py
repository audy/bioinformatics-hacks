#!/usr/bin/env python3

# # kraken-table
# 
# Generates a table from [Kraken](https://ccb.jhu.edu/software/kraken/)
# output(s). Like [kraken-biom](https://github.com/smdabdoub/kraken-biom) but
# doesn't require you to install biom-format, SciPy and Numpy just to generate a
# table.
# 
# ## Usage
# 
# ```
# ./kraken-table.py \
#   --inputs \
#   kraken_output_1.txt \
#   kraken_output_2.txt \
#   > otus.csv
# ```

import argparse
import logging
from csv import DictWriter
from collections import defaultdict

def parse_args():
    '''
    return arguments
    >>> args = parse_args()

    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default='/dev/stderr',
                        help='log file (default=stderr)')
    parser.add_argument('--output', default='/dev/stdout')
    parser.add_argument('--inputs', nargs='*', default=[])
    return parser.parse_args()


def parse_kraken_file(handle):
    for line in handle:
        line = line.strip().split("\t")

        yield {
            'classified': { 'C': True, 'U': False }[line[0]],
            'read_id': line[1],
            'ncbi_taxid': line[2],
            'length': int(line[3]),
            'assignments': line[4].split()
        }



def main():
    '''
        >>> main() # stuff happens
    '''

    args = parse_args()
    logging.basicConfig(filename=args.log, level=logging.INFO)

    input_otu_counts = defaultdict(lambda: defaultdict(lambda: 0))
    field_names = set()

    for input in args.inputs:
        with open(input) as handle:
            kraken_data = parse_kraken_file(handle)

            for row in kraken_data:
                field_names.add(row['ncbi_taxid'])
                input_otu_counts[input][row['ncbi_taxid']] += 1

    field_names = ['input'] + sorted([ i for i in field_names ])

    with open(args.output, 'w') as handle:
        writer = DictWriter(handle,
                            fieldnames=field_names)

        writer.writeheader()

        for input, otu_counts in input_otu_counts.items():
            otu_counts['input'] = input
            writer.writerow(otu_counts)




if __name__ == '__main__':
    main()
