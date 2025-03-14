#!/usr/bin/env python

#import RegEx
import re 
from typing import cast
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("-k", help="kmer_size")
    parser.add_argument("-f", help="input fasta file", type = str) #type: str
    parser.add_argument("-o", help="table file name")
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


with open(args.o, "w") as table:
    # first_row = (f’| Number of contigs: | Total genome length: | Max contig length: | Mean contig length: | Minimum contig length: | Mean depth of coverage: | N50 |\n’)
    # second_row = (f’| ---: | :---: | :---: | :---: | :---: | :---: | :---: |\n’)
    # third_row = (f’| {num_contigs} | {genome_len} | {max_len} | {mean_len} | {min_len} | {mean_cov} | {N50} |’)
    table.write(f"| Number of contigs: | Total genome length: | Max contig length: | Mean contig length: | Minimum contig length: | Mean depth of coverage: | N50 |\n")
    table.write(f"| ---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
    table.write(f"| {num_contigs} | {genome_len} | {max_len} | {mean_len} | {min_len} | {mean_cov} | {N50} |")
