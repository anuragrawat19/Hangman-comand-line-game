import string # importing string module which deals with the  the text data
from words import choose_word # imprting a "choose_word()" function  from the file named" words" which return a random new secret_word
from images import IMAGES # importing a IMAGES list from a file images

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: it is a secret word that user has to guess
    letters_guessed: this is the list that contains all the letters that are guessed 
 
    '''
    if secret_word == get_guessed_word(secret_word, letters_guessed): #   returns: return will be true if a letter guesses by user is in the secret_word
        
        return True

    return False # otherwise it will return the false if user guess it wrong 

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai



def get_guessed_word(secret_word, letters_guessed):# return the list of all those number which are guessed

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    #this function  the the list of all the letters that are not guessed yet
    import string
    all_letters = string.ascii_lowercase
    letters_left=''
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left+=letter
    return letters_left

def ifvalid(guess):# to check whether the  guessed token is valid character or not 
    if len(guess)!=1:
        return False
    if not guess.isalpha(): # if the  guessed token is not a alphabet it will return false
        return False
    return True

def get_hint(secret_word,letters_guessed): #this function will give a player hint of that letter which is present in the  secret word 
    import random
    letters_not_guessed=[]

    i=0
    while (i<len(secret_word)):
        letter=secret_word[i]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        i+=1
    return random.choice(letters_not_guessed)


    

def hangman(secret_word): 
    '''
    secret_word is a string, the secret word to guess.

    Hangman game starts like this :

    *  the player is introduced to the length of the secret word before game starts

    * in every round user is asked to guess a letter and whether is guess letter is correct or not  according to that message is displayed
   

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print "you have 8 chances if you guess the aplhabet 8 times then your one chance will be deducted and when you guess wrong 8 times then you will lost the game "
    print""
    user_difficulty_choice=raw_input("which difficulty level do you want to play?\na)\tEasy\nb)\tMedium\nc)\tHard\n\n Choose in terms of a,b,c")
    

    total_lives=remaining_lives=8
    image_selection_list_indices=[0,1,2,3,4,5,6,7]

    if user_difficulty_choice not in ["a","b","c"]:
        print "Apki choice invalid hai isiliye hmm easy level se start kr rhe hai.\n"
    else:
        if user_difficulty_choice=="b":
            total_lives=remaining_lives=6
            image_selection_list_indices=[0,2,3,5,6,7]
        elif user_difficulty_choice=="c":
            total_lives=remaining_lives=4
            image_selection_list_indices=[1,3,5,7]

    letters_guessed = []
   

    while (remaining_lives>0):
    
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters

        guess = raw_input("Please guess a letter: ")
        

        if guess=="hint":
            letter =get_hint(secret_word,letters_guessed)
        elif (not ifvalid(guess)):
            print "not a valid input"
            continue
        else:
            letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""

        else:
            print IMAGES[image_selection_list_indices[total_lives-remaining_lives]]
            print"remaining lives : ", remaining_lives
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            remaining_lives-=1
            print ""

    print "Sorry, you ran out of guesses. The word was " + str(secret_word) + "."
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
