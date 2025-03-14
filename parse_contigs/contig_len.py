#!/usr/bin/env python

#import RegEx
import re 
from typing import cast
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("-k", help="kmer_size")
    parser.add_argument("-f", help="input fasta file", type = str) #type: str
    parser.add_argument("-o", help="out file TSV of contig distribution")
    return parser.parse_args()

args = get_args()

out_file = args.o
file = args.f
k_size = int(args.k)

k_length_lst = []
kmer_cov_lst = []
n_len_lst = []
n_cov_lst = []
contig_counter = 0
total_contig_len = 0
contig_lengths = 0

with open (file) as fh1:
    for line in fh1:
        if ">" in line: #only calls header lines
            contig_counter +=1 #counts the number of headers therefore number of contigs
            k_len = re.search('length_([0-9]+)', line) #regex finds 'length_' followed by any set of numbers and 'lassos' numbers 
            k_len = cast(re.Match[str], k_len) #removes type error, bc I know it will always return a match and not a None
            klength = int(k_len[1]) #takes what I lassoed at index 1 wich is the number 
            k_length_lst.append(klength) #appends to list  
            my_cov = re.search('cov_([0-9.]+)', line) #include decimal to account for floats 
            my_cov = cast(re.Match[str], my_cov)
            cov = float(my_cov[1])
            kmer_cov_lst.append(cov)
            #adjust length to account for nt length 
            n_len = int(klength + k_size - 1) #derived from kcount formula
            n_len_lst.append(n_len) #append to list
            n_cov = (cov * n_len) / klength
            n_cov_lst.append(n_cov) 

sort_len = sorted(n_len_lst, reverse= True) #sort from lasrgest to smallest (for N50)
num_contigs = len(n_len_lst)
genome_len = sum(n_len_lst)
max_len = sort_len[0]
mean_len = genome_len/num_contigs
min_len = sort_len[-1]

counter_n50 = 0 
for leng in sort_len: 
    if counter_n50 < genome_len/2:
        counter_n50 += leng
        N50 = leng 
    else: 
        break 

numerator = 0
for i in range(len(n_len_lst)): #list must not be sorted so the index of the len matches the index of the cov
    numerator += (n_len_lst[i] * n_cov_lst[i])
mean_cov = numerator/(genome_len)
# print("Mean coverage:", mean_cov)
# print("genome Length:", genome_len)
# print("max contig len:", max_len)
# print("mean length:", mean_len)
# print("min len:", min_len)
# print("N50:", N50)
with open (f"Stats_Report_{args.o}", "w") as out:
    out.write(f"Number of Contigs: {num_contigs}\n")
    out.write(f"Genome Length: {genome_len}\n")
    out.write(f"Max Contig Length: {max_len}\n")
    out.write(f"Mean Contig Length: {mean_len}\n")
    out.write(f"Min Contig Length: {min_len}\n")
    out.write(f"Mean Coverage: {mean_cov}\n")
    out.write(f"N50: {N50}")


#binning using floor division : 
#floor divide by 100 and mult by 100 
#store in dictionary 
contig_len_bin_dict = dict()
# print(n_len_lst)
for contig_len in n_len_lst:
    bin_val = contig_len//100 * 100
    if bin_val in contig_len_bin_dict:
       contig_len_bin_dict[bin_val] += 1
    else:
        contig_len_bin_dict[bin_val] = 1

sorted_bin_dict = sorted(contig_len_bin_dict)

#create  file that the graph uses NO HEADERS DO NOT TURN IN 
with open ("Dist_File_GRAPH", "w") as out:
    for bin in sorted_bin_dict: 
        out.write(f"{bin} {contig_len_bin_dict[bin]}\n")

#create TSV file that will be submitted WITH HEADERS 
with open (f"{out_file}.tsv", "w") as out:
    out.write(f"Contig Length\tNumber of Contigs in this Catagory\n")
    for bin in sorted_bin_dict: 
        out.write(f"{bin}\t{contig_len_bin_dict[bin]}\n")
# Graph distribution: 

from matplotlib import pyplot as plt

x = []
y = []

with open ("Dist_File_GRAPH") as distribution:
    for line in distribution:
        spline = line.split()
        size = int(spline[0])
        frequency = int(spline[1])
        x.append(size)
        y.append(frequency)

fig, ax = plt.subplots()
plt.bar([q/100 for q in x],y)
plt.xlabel("Contig Size Bin")
plt.ylabel("Number of Contigs in Bim")
plt.title(f"Distribution of Contig Sizes_K{args.k}")
plt.savefig(f"{out_file}.png")
        


