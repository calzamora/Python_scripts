#!/usr/bin/env python

genome_size = 2000000 # hand calculated from fosmid sizes 40*50 kb
file1 = "/projects/bgmp/calz/bioinfo/Bi621/PS/ps6-calzamora/800_3_PE5_interleaved.fq_1"
file2 = "/projects/bgmp/calz/bioinfo/Bi621/PS/ps6-calzamora/800_3_PE5_interleaved.fq_2"
file3 = "/projects/bgmp/calz/bioinfo/Bi621/PS/ps6-calzamora/800_3_PE5_interleaved.fq.unmatched"

k = 49
NT = 0
CK = 0
# CK2 = 0
# CK3 = 0 
lines = 0 
C = 98.59 #total nucleotides / 2000000


#calculate the kmer val of paired fq.1 
with open(file1) as pair1:
    for i, line in enumerate(pair1):
        lines += 1 #coult all lines (for total record number )
        line = line.strip()
        if (i+1)%4 ==2: #select only seq lines 
            NT+=len(line) #iterate the total line length
            CK += (C*(len(line)-k + 1))/len(line) #calc the  CK for this file and add to running total 


#calculate the kmer val of paired fq.2
with open(file2) as pair1:
    for o, seq in enumerate(pair1):
        lines += 1
        seq = seq.strip()
        if (o+1)%4 ==2:
            NT+=len(seq)
            CK += (C*(len(seq)-k + 1))/len(seq)


#calculate the kmer val of unmapped
with open(file3) as unmatched:
    for b, nt in enumerate(unmatched):
        lines += 1
        nt = nt.strip()
        if (b+1)%4 ==2:
            NT+=len(nt)
            CK += (C*(len(nt)-k + 1))/len(nt)


records = lines/4

expected_cov = CK/records
print(expected_cov)