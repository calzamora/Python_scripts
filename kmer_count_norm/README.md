# KMER Counting and Normalization

## kmer_count
This script will kmerize a short read FASTQ file and could the number of kmers per occurance.
### Usage:
```
kspec.py -k [K-MER LENGTH] -l[READ LENGTH] -f [FILE NAME]
```

### Input: 
- ```-f``` Specify seq file pathway.
- ```-k``` Specify user desired kmer size.
- ```-l``` Specify read length of Illumina seq file.

### Output:
- **.txt file** denoting the kmer frequency (number of times a kmer is seen)  
- **.png image** visualizing this distribution. 

### Dependencies: 
1) matplotlib.pyplot
2) bioinfo.py (stored in this directory)
3) argparse

## kmer_normalization
This script normalizes k-mer coverage of the input FSATQ and saves them to a new FASTQ file.

### Usage
```
knorm.py -f [FILE PATHWAY] -c [COVERAGE LIMIT] -k [KMER SIZE] -l [READ LENGTH] -o [OUTPUT FILE]
```

### Input: 
- ```-c``` Specify the coverage limit
- ```-f``` Specify the filename
- ```-k``` Specify the k-mer size
- ```-l``` Specify the read length
- ```-o``` Specify the output file name

### Output:
- **.fq file** with normalized kmer coverage. 

### Dependencies: 
1) bioinfo.py (stored in this directory)
2) argparse