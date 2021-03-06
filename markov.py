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
        second_word = current_tuple[1]
        third_word = r_choice(chains.get(current_tuple))

        if len(new_string + first_word) > 139:
            break 
        new_string = new_string + " " + first_word
        if len(new_string + second_word) > 139: 
            break 
        new_string = new_string + " " + second_word
        if len(new_string+ third_word) > 139: 
            break

        new_string = new_string + " " + third_word

        current_tuple = (second_word, third_word)

    # print len(new_string)
    return new_string

def main():
    # if running from cmd line use args to choose text file
    # script, filename = argv

    #if calling this script from tweet_machine, put name of text file here
    filename = "greenEggs.txt"

    open_file = open(filename)
    input_text = open_file.read().split()
    # print input_text
    chain_dict = make_chains(input_text)    # convert text into dictionary of tuple keys and list values
    # print chain_dict
    # feed dictionary into text generator
    random_text = make_text(chain_dict)
    return random_text

if __name__ == "__main__":
    main()


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