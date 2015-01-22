#!/usr/bin/env python

from sys import argv
from random import choice as r_choice
#import random as r
#import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    chains_dict = {}
    # create a tuple to hold the key and a list to hold the value
    # key should be (first word, second word)
    # value should be [word that follows tuple, word that follows tuple, etc] 
    for i in range(len(corpus)-2):
        # if tuple not already in dict as key, add it and assign value
        if (corpus[i], corpus[i+1]) not in chains_dict.keys():
            chains_dict[(corpus[i], corpus[i+1])] = [corpus[i+2]]
        # otherwise, if tuple is already in dict as key,
        # append new value to existing value list
        else:
            value_list = chains_dict.get((corpus[i], corpus[i+1])) # get value from key (which is a tuple & bind to name value_list
            value_list.append(corpus[i+2])                         # append the third word from the current position to the value list
    return chains_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    new_string = ""
    # pick a key
    first_tuple = r_choice(chains.keys())
    first_word = first_tuple[1]
    print "first word is: ", first_word
    second_word = r_choice(chains.get(first_tuple))
    print "second word is: ", second_word
    new_string = new_string + first_word + " " + second_word
    print "new string is: ",new_string
    print type(new_string)
    # get a random word from the dict values

    # while this tuple is in the set of 


    #return "Here's some random text."

    #FIXME: write out next steps in English
    # Next step: turn string generator into a loop to create new word combinations
    # Will be a while loop

def main():
    script, filename = argv

    # Change this to read input_text from a file
    open_file = open(filename)
    input_text = open_file.read().split()
    # print input_text

    chain_dict = make_chains(input_text)
    #print chain_dict
    random_text = make_text(chain_dict)




    # print random_text

if __name__ == "__main__":
    main()