#!/usr/bin/env python

# Author: <YOU> <optional@email.address>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.1"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = set('ATCGNatcgn')
RNA_bases = set('AUCGNaucgn')

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter)-33

def qual_score(phred_score: str) -> float:
    '''Write your own doc string'''
    total=0 #total starts at 0 so we have a number to add the first ph_score to. 
    for char in phred_score: #for each character in the string phred_score
        ph_score = convert_phred(char) #converts ascii to numerical phred score       
        total = total + ph_score #same as total+=ph_score     
    return total / len(phred_score) #returns total sum of all phred scores divided by the length of the string

def validate_base_seq():
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    pass

def gc_content():
    '''Returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    assert validate_base_seq(DNA), "String contains invalid characters - are you sure you used a DNA sequence?"    
    DNA = DNA.upper()
    return (DNA.count("G")+DNA.count("C"))/len(DNA)

def calc_median(lst: list) -> float:
    N = 0
    if len(lst) % 2 != 0: 
        pos = len(lst) // 2
        # for position, number in enumerate lst: 
        median = lst[pos]
        # print(median)
    else: 
        upper = (len(lst) // 2)
        lower = (len(lst) // 2) - 1
        median = (lst[upper] + lst[lower]) / 2
        # median = 
    return(median)
    pass

def oneline_fasta():
    '''docstring'''
    pass

if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")
