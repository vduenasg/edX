# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/NetzeK/Documents/6.00.1x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    if (len(secretWord) == 0 and len(lettersGuessed) == 0) or (len(secretWord) == 0 and len(lettersGuessed) != 0):
        return True
    else:
        if secretWord[0] in lettersGuessed:
            lettersGuessed.remove(secretWord[0])
        else:
            return False
        return isWordGuessed(secretWord[1:], lettersGuessed)
    '''
    secretWord = 'apple' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print isWordGuessed(secretWord, lettersGuessed)
    False
    '''


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(secretWord) == 0:
        return ''
    else:
        if secretWord[0] in lettersGuessed:
            return secretWord[0] + getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            return '_ ' + getGuessedWord(secretWord[1:], lettersGuessed)
    '''
    secretWord = 'apple' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print getGuessedWord(secretWord, lettersGuessed)
    '_ pp_ e'
    '''


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    import string
    Letters = string.ascii_lowercase
    for i in Letters:
        if i not in lettersGuessed:
            availableLetters += i
    return availableLetters
    '''
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print getAvailableLetters(lettersGuessed)
    abcdfghjlmnoqtuvwxyz
    '''
    

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
    numGuesses = 8
    lettersGuessed = []
    lettersGuessed_B = []
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord)) +' letters long.'   
    while numGuesses > 0:
        print '-----------'
        print 'You have '+ str(numGuesses) + ' guesses left.'
        print 'Available Letters: ' + getAvailableLetters(lettersGuessed_B)
        guess = raw_input('Please guess a letter: ')
        numGuesses -= 1
        guess = guess.lower()
        if guess in lettersGuessed_B:
            numGuesses += 1
            lettersGuessed = lettersGuessed_B[:]
            print 'Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed)
        
        elif guess in secretWord:
            numGuesses += 1
            lettersGuessed_B.append(guess)
            lettersGuessed = lettersGuessed_B[:]
            print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed_B.append(guess)
            lettersGuessed = lettersGuessed_B[:]
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
        
        if isWordGuessed(secretWord, lettersGuessed):
            print '------------'
            print 'Congratulations, you won!'
            break
    if numGuesses == 0:
        print '------------'
        print 'Sorry, you ran out of guesses. The word was ' + secretWord+'.'
        








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
