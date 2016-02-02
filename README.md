# Synonyms for Solr search

> Script to automatically download and parse synonyms into a format campatible with Solr

### MeSH

1. Download and parse MeSH

   ```
   ./get-mesh-synonyms.sh
   ```

2. Append the content of `data/mesh-synonyms-solr.txt` to your core's `synonyms.txt`. E.g. `refinery/solr/core/synonyms.txt`
