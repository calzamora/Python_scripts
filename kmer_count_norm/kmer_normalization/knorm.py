#!/usr/bin/env python
import argparse
import bioinfo

def get_args():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("-c", help="spevify coverage limit ", type = int) #type: str 
    parser.add_argument("-k", help="specify kmer size", type = int) #type: str #JASON ADDED: "--kmer-size", metavar='K', [BEFORE HELP OPTION]
    parser.add_argument("-f", help="specify the input filename", type = str) #type: str
    parser.add_argument("-l", help="specify read length", type = int)#type:str
    parser.add_argument("-o", help="specify output file name", type = str)#type:str

    return parser.parse_args()

args = get_args()
#initialize an empty dict: 

#set global variables:
k_coverage = args.c
in_file_name = args.f
k_occurance = dict()
kcount = int(args.l) -int(args.k) + 1
# coverage = []

#open the output file that we will be writing to: 
with open(args.o, "w") as out_file, open(in_file_name, "r") as in_file:
    #set each line of the first record 
    while True:
        header = in_file.readline()#.strip()
        seq = in_file.readline()#.strip()
        plus = in_file.readline()#.strip()
        qscore = in_file.readline()#.strip()
        # break statement to get out of loop
        if header == "":
            break
        #kmerize and add to dictionary
        for j in range(kcount):
            kmer = (seq[j: args.k + j])
            if kmer in k_occurance:
                k_occurance[kmer] += 1
            else: 
                k_occurance[kmer] = 1
        #initialize a list 
        coverage = []
        #re-kmerize 
        for j in range(kcount):
             kmer = seq[j: int(args.k) + j]
             #if that kmer is in the dictionary, append the VALUE of that key to the list 
             if kmer in k_occurance:
                coverage.append(k_occurance[kmer])
        #calculate median of SORTED list
        median = bioinfo.calc_median(sorted(coverage))
        #if the med is below the cut off: append it to the list
        if median <= args.c: 
            out_file.write(header)
            out_file.write(seq)
            out_file.write(plus)
            out_file.write(qscore)
    #add a new line to the last seq to get it to match the 5x file exactly
    out_file.write('\n')

