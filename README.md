# Knuth-Morris-Pratt-app

Design a python script that opens a web service. The web services internally stores the genome of SARS-COV-2 (https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?report=fasta). The web service exposes an API that allows the user to upload a short nucleotide sequence. As a results, the web server returns the number of occurrences of the small sequence in the genome of SARS-CoV-2.

# Knuth Morris Pratt algorithm

In string computation, the exact pattern matching problem is the problem of finding all the occurences of a pattern (string) P, in a text (string) S, where usually P is much shorter than S. For example the pattern could be the world “stella” and the text the whole Divina Commedia, or P can be the CCATTGTG motif and the text the human genome. One strategy to speed up the computation is to create an index on the pattern P and use this index to scan the text S in a more efficient way. The Knuth-Morris-Pratt algorithm uses this approach. It first of all builds an index on P and then uses it to scan S, applying simple rules to the index to decide how to shift the pattern.
