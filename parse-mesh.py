#!/usr/bin/env python

# Author: Fritz Lekschas
# Date: 2016-02-02
#
# parse into a Solr compatible format

import sys


def parse_mesh(input, output):
    synonyms = ''

    with open(output, 'w') as o:
        o.truncate()
        with open(input, 'r') as f:
            for line in f:
                line = line.rstrip()
                if line[:5] == 'MH = ':
                    # Write previous synonyms to output
                    if len(synonyms):
                        o.write(synonyms + '\n')
                    synonyms = line[5:].rstrip()
                else:
                    lim = -1
                    if line[:8] == 'ENTRY = ':
                        lim = 8
                    elif line[:14] == 'PRINT ENTRY = ':
                        lim = 14

                    if lim >= 0:
                        synonym = line[lim:].rstrip()
                        end = synonym.find('|')

                        if end >= 0:
                            synonym = synonym[:end]

                        synonyms = synonyms + ','
                        for phrase in reversed(synonym.split(',')):
                            synonyms = synonyms + phrase.strip() + ' '
                        # Remove last white space
                        synonyms = synonyms[:-1]


#############
# MAIN      #
#############

def main():
    input = './data/mesh-ascii.txt'
    output = './data/mesh-synonyms-solr.txt'

    parse_mesh(input, output)

    sys.exit()

if __name__ == "__main__":
    main()
