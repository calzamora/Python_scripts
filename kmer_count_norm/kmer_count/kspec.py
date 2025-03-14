#!/usr/bin/env python
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("-k", help="k-mer size ") #type: str
    parser.add_argument("-l", help="specify read length") #type: str
    parser.add_argument("-f", help="specify the filename") #type: str
    return parser.parse_args()

args = get_args()
# print(args.k, args.l, args.f)

#initialize a dictionary where the 
# k-mers (ex:ATCGT) are the KEYS  type : string
# number of occurances are the VALUES type : int 
kmer_occurances_dict = dict()
kcount = int(args.l) -int(args.k) + 1

with open (args.f, "r") as fq1:  #open the file given in the -f flag 
    for i, seq in enumerate(fq1): # set the index locaion equal to i and the contents to seq
        if i % 4 == 1: # selects for just the sequence lines and filters out the rest of the fastq record 
            for j in range(kcount): # initializing j as 0 and incrimenting through every loop. range(kcount) = range [0:3] so it only sets the key
                #if we are are at poition 0,1, or 2 in the sequence. this prevents us from running off the end of the sequence. (think back to possible kmers based on seq length)
                kmer = (seq[j: int(args.k) + j]) # set the key equal to the sequence of kmer length k starting at j 
                if kmer in kmer_occurances_dict:
                    kmer_occurances_dict[kmer] += 1 # if the key is in the dict, call existing key and incriment the value by 1
                else:
                    kmer_occurances_dict[kmer] = 1
                    # kmer_occurances_dict.setdefault(j_dawg, 1) # if the key does NOT exist, add it and set the value = to 1


            
    # print(kmer_occurances_dict)

#second dictionary to hold distribution of K-mer occurranes
#key = # of occurrances (int)
#value = # of kmers that occur that amount

dist_dict =  dict()
#initialize 
for occurance in kmer_occurances_dict:
    key = kmer_occurances_dict[occurance]
    if key in dist_dict:
        dist_dict[key] += 1
    else:
        dist_dict[key] = 1

sorted_dist_dict = sorted(dist_dict)
#creates a list of the KEYS of the dict and asigns to sorted_dist_dict
# print(sorted_dist_dict)

with open ("hist_10x.txt", "w") as file:
    file.write(f"kmer frequency\tNumber of kmers int his category\n")
    for key in sorted_dist_dict:
        file.write(f"{key}\t{dist_dict[key]}\n")
        #print the key (value from sorted_dist_dict) and the value asigned to that key


with open ("graph_file", "w") as file:
    # file.write(f"kmer frequency\tNumber of kmers int his category\n")
    for key in sorted_dist_dict:
        file.write(f"{key}\t{dist_dict[key]}\n")
        #print the key (value from sorted_dist_dict) and the value asigned to that key

import matplotlib.pyplot as plt

x = []
y = []

with open ("graph_file") as kmer:
    for line in kmer:
        spline = line.split()
        freq = int(spline[0])
        number = int(spline[1])
        x.append(freq)
        y.append(number)

# print(x)
# print(y)
        
plt.bar(x, y,width=2,linewidth=1)

plt.xlim(0,10000)
plt.yscale("log")

plt.xlabel("Number of Kmers per Occurance")
plt.ylabel("Occurance")
plt.title("Number of Kmers")

plt.savefig("hist_10x.png")