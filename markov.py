#!/usr/bin/env python

from sys import argv
from random import choice as r_choice

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
    current_tuple = r_choice(chains.keys())
    while current_tuple in chains.keys():
        first_word = current_tuple[0]
        # print "first word is: ", first_word
        second_word = current_tuple[1]
        # print "second word is: ", second_word
        third_word = r_choice(chains.get(current_tuple))
        # print "third word is: ", third_word

        new_string = new_string + " " + first_word + " " + second_word + " " + third_word
        # print "new string is: ",new_string
        current_tuple = (second_word, third_word)
    
    return new_string
    # From the first and second word, find third word 
    # - which is randomly picked from value_list 
    # associated with the current (first word, second word) tuple key 
    # get a random word from the dict values
    # while this tuple is in the set of 
    # turn string generator into a loop to create new word combinations

def main():
    script, filename = argv

    open_file = open(filename)
    input_text = open_file.read().split()

    # convert text into dictionary of tuple keys and list values
    chain_dict = make_chains(input_text)
    # print chain_dict
    # feed dictionary into text generator
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()

# works!  but makes one giant wall of text. needs more work to refine output.

"""
Extra Credit

Do any of the following

- See what happens when you mix two different authors together as a single source
- Modify the program to allow any number of words to use as keys, ie: choose the size 
of your n-gram used in your chain
- Create a new Twitter persona and wire up your markov program with the twitter module
(import twitter) to produce random tweets. (docs are here). The twitter module is already 
installed on the lab machines. NOTE: Do not publish your Twitter API credentials to GitHub! 
Create a file with your credentials and then make Git ignore it with .gitignore
"""