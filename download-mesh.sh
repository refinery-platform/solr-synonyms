#!/bin/bash

# Author: Fritz Lekschas
# Date: 2016-02-01
#
# Download MeSH TXT file

mkdir -p ./data
curl -L -o ./data/mesh-ascii.txt ftp://nlmpubs.nlm.nih.gov/online/mesh/.asciimesh/d2016.bin
