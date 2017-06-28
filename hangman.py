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
    # FILL IN YOUR CODE HERE...
    answerList = []

    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            answerList.append('T')
        else:
            answerList.append('F')
    if 'F' in answerList:
        return False
    else:
        return True 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    currentGuess = ['_ '] * len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            currentGuess[i] = secretWord[i]
    return ''.join(currentGuess)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lettersAvailable = list(string.ascii_lowercase)
    
    for letter in lettersGuessed:
        if letter in lettersAvailable:
            lettersAvailable.remove(letter)
    return ''.join(lettersAvailable)
    

def hangman(secretWord):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    guessesLeft = 8
    gameover = False
    alphabet = list(string.ascii_lowercase)
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    
    while gameover != True:
        
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guessedLetter = input('Please guess a letter: ')
        
        while guessedLetter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            print('You have ' + str(guessesLeft) + ' guesses left.')
            print('Available letters: ' + getAvailableLetters(lettersGuessed))
            guessedLetter = input('Please guess a letter: ')
        
        if guessedLetter not in alphabet:
            print("Oops! You're input was not a letter: " + getGuessedWord(secretWord, lettersGuessed))
            guessedLetter = input('Please guess a letter: ')
            print('-------------')
            
        elif guessedLetter in secretWord:
            lettersGuessed += guessedLetter
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Congratulations, you won!')
                gameover = True
        
        else:
            lettersGuessed += guessedLetter
            guessesLeft -= 1
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            if guessesLeft <= 0:
               print('Sorry, you ran out of guesses. The word was: ' + secretWord + '.')
               gameover = True
               
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)