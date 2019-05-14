import string
import random

def load_words():
    """
    this function helps in loading a words from a file named" words.text"
    """
    print "Loading word word list from file........"
    inFile=open("words.txt","r")
    line=inFile.read()
    word_list=string.split(line)
    print "  ",len(word_list),"words loaded.\n"
    return word_list


def choose_word():
    """
    word_list (list): list of words (strings)
    this function will return a random word from a list and will store it into a varibale "secret_word" 
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
