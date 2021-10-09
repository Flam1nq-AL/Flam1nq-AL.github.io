import os

guess_list = []
word = ''
blanks = []
index = ''
displays = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']


def guess_letter(x, word, blanks):
    indexes = []
    # Check if guess is in word
    if x in word:
        for i in word:
            # finding all occurences of guess in word
            for i in range(len(word)):
                if word[i] == x:
                    indexes.append(int(i))
        # replacing the blanks with correct letter guesses
        for a in indexes:
            blanks[a] = x

# checks if guess is in word for a boolean return


def correct_guess(x, word):
    if x in word:
        return True
    else:
        return False

# displays the current state of the word with or without blanks


def display(guesses, blanks):
    print(displays[guesses])
    print(*blanks)

# asks user to input word to be guessed


def get_word():
    word = str(input('Please enter the word to be guessed.').lower())
    while any(char.isdigit() for char in word):
        word = str(input('That is not a valid word. Please try again.').lower())
    return word


def play():
    guesses = 0
    blanks = []
    correct = False
    word = get_word()
    # initialising word with number of blanks being the same as the length of the word
    for i in range(len(word)):
        blanks.append('_')
    display(guesses, blanks)
    # Giving user guesses up to a limit of 6
    while guesses < 6:
        guess = str(input('Please enter your letter guess.').lower())
        # error checking for guess being a string and also a single letter
        while type(guess) != str and len(guess) != 1:
            guess = str(
                input('That is not a single letter. Please re-enter your letter guess.'))
        guess_letter(guess, word, blanks)
        # if the guess was in the word, the number of guesses does not increase
        if correct_guess(guess, word) and guess not in guess_list:
            guess_list.append(guess)
        else:
            if guess in guess_list:
                print('You have already guessed that letter. Please try again.')
            else:
                guesses += 1
                guess_list.append(guess)
        display(guesses, blanks)
        # No more blanks means that all letters have been guessed
        if '_' not in blanks:
            correct = True
            break
    if correct == True:
        print(f'You win! You guessed the word with {6-guesses} guesses left!')

    else:
        print('You lose! You did not guess the word!')
    play_again = str(input('Would you like to play again? (Y or N)').lower())\
        # error checking for the user's choice of playing again or not
    while play_again != 'y' and play_again != 'n':
        play_again = str(input(
            'That is not a valid response. Would you like to play again (Y or N)').lower())
    if play_again == 'y':
        # Reset crucial variables to allow the game to play again using recursion
        correct = False
        guesses = 0
        play()


play()
