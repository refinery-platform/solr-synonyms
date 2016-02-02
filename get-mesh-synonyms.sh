#!/bin/bash

# Author: Fritz Lekschas
# Date: 2016-02-01
#
# Download MeSH and parse into a Solr compatible format

./download-mesh.sh && ./parse-mesh.py
