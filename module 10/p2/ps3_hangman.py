# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    s = 0
    for i in range(0, len(secretWord), 1):
        if secretWord[i] in lettersGuessed:
         s += 1
        else:
           continue
    if s == len(secretWord):
        return True        
    else:
        return False
def getGuessedWord(secretWord, lettersGuessed):
    '''secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string1 = ''
    for i in range (0, len(secretWord), 1):
        if secretWord[i] in lettersGuessed:
            string1 += secretWord[i]
        else:
            string1 += '___'
    return string1            
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = []
    str1 = string.ascii_lowercase
    for i in str1:
        if i not in lettersGuessed:
            letters.append(i)
    return "".join(letters)

def testinput(guess):
    if len(guess) > 1 or (guess <= 'a' and guess >= 'z'):
        print("INVALID INPUT")
        return False
    return True    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("WELCOME")
    letter_guessed = []
    count = 0
    print("I m thinking of the word which is ", len(secretWord), "letters")
    print("..................")
    temp = False
    max_guess = len(secretWord) + 3
    print(getGuessedWord(secretWord,letter_guessed))
    while max_guess != 0:
        print("you have:",max_guess, "left")
        print("available letters:", getAvailableLetters(letter_guessed))
        guess = input("please guess a letter:")
        max_guess -= 1

        if not testinput(guess):
            continue
        letter_guessed.append(guess)
        temp = isWordGuessed(secretWord,letter_guessed)
        if temp:
           break
        print(getGuessedWord(secretWord,letter_guessed))
    if temp == 'True':
        print("Congrats you guessed the right word")
    else:    
        print("try again")               
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
