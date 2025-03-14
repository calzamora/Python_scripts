# Parse Contig Lengths
## contig_len.py 
This script will parse a standard fasta file, and output basic alignment statistics:

### Usage: 
```
contig_len.py -k [KMER SIZE] -f [FILE PATHWAY TO FASTA] -o [OUT TSV FILE PREFIX]
```
### Input: 
- ```-f``` Specify fasta file pathway.
- ```-k``` Specify user desired kmer size.
- ```-o``` out TSV prefix.

### Output: 

1) TSV file containing: 
    * the number of contigs
    * the total length of the genome assembly across the contigs
    * the maximum contig length
    * the mean contig length
    * the minimum contig length
    * the mean depth of coverage for the contigs
    * the N50 value of assembly

2) PNG image of the distribution of contigs

### Dependencies: 
- re 
- typing
- argparse

## contig_stats_table.py
This file outputs above statistics as table
### Usage
```
contig_len.py -k [KMER SIZE] -f [FILE PATHWAY TO FASTA] -o [OUT TSV FILE PREFIX]
```
### Input: 
- ```-f``` Specify fasta file pathway.
- ```-k``` Specify user desired kmer size.
- ```-o``` out table prefix.

### Output: 

1) Table file containing: 
    * the number of contigs
    * the total length of the genome assembly across the contigs
    * the maximum contig length
    * the mean contig length
    * the minimum contig length
    * the mean depth of coverage for the contigs
    * the N50 value of assembly

### Dependencies: 
- re 
- typing
- argparse

## expected_cov.py
This script outputs to std out the expected coverage for kmer size 49 for 3 hard coded fastq files (paired end + unmatched)
### Usage
```
expected_cov.py
```
### Input: 
expected  coverage to standard out

### Output: 
expected kmer size 49 coverage to std out