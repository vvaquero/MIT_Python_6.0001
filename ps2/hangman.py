# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise

    Test:
    print(is_word_guessed('test',['d', 'f', 't', 'e', 's']))
    '''


    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.

    Tests:
    secret_word = 'apple'
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(get_guessed_word(secret_word, letters_guessed))
    '''


    out_string = list(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            out_string[i] = '_ '

    return ''.join(out_string)





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.

    Tests:
    letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(get_available_letters(letters_guessed))
    '''

    import string
    dict = string.ascii_lowercase

    for letter in letters_guessed:
        if letter in dict:
            dict = dict.replace(letter, '')

    return dict

def calculate_score(guesses_remaining, secret_word):
    unique_letters = len(set(secret_word))
    return guesses_remaining * unique_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')

    num_guesses_left = 6
    num_warnings = 3
    letters_guessed = []
    get_available_letters(letters_guessed)

    while num_guesses_left > 0:
        print('-------------')
        print(f'You have {num_guesses_left} guesses left.')
        # Getting correctly a guessed letter
        print(f'Available Letters: {get_available_letters(letters_guessed)}')

        correct_letter = False
        while not correct_letter:
            my_letter = input('Please guess a letter: ')
            if str.isalpha(str.lower(my_letter)) and len(my_letter) == 1 and my_letter not in letters_guessed:
                correct_letter = True
                letters_guessed.append(my_letter)
                # print(f'Letters guessed {letters_guessed}')
            else:
                num_warnings -= 1
                part_sol = get_guessed_word(secret_word, letters_guessed)
                if my_letter in letters_guessed:
                    print(f'Oops! You\'ve already guessed that letter. You have {num_warnings} warnings left: {part_sol}')
                else:
                    print(f'Oops! That is not a valid letter. You have {num_warnings} warnings left: {part_sol}')

                if num_warnings == 0:
                    print('---> You lose a guess! ')
                    num_warnings = 3
                    # num_guesses_left -= 1
                    break

        if correct_letter and num_guesses_left > 0:
            part_sol = get_guessed_word(secret_word, letters_guessed)

            if my_letter in secret_word:
                print(f'Good guess: {part_sol}')
            else:
                print(f'Oops! That letter is not in my word: {part_sol}')
                num_guesses_left -= 1

            if is_word_guessed(secret_word,letters_guessed):
                print('Congratulations, you won!')
                print(f'Your total score for this game is: {calculate_score(num_guesses_left, secret_word)}')
                break

        elif num_guesses_left > 0:
            num_guesses_left -= 1

        if num_guesses_left <= 0:
            print(f'Sorry, you ran out of guesses. The word was {secret_word}')
            return


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:

    Tests:
    print(match_with_gaps("te_ t", "tact"))
    print(match_with_gaps("a_ _ le", "banana"))
    print(match_with_gaps("a_ _ le", "apple"))
    print(match_with_gaps("a_ ple", "apple"))
    '''

    # remove spaces from my word
    my_word2 = my_word.replace(" ", "")
    list_used_letters = []  # contains the letters represented by '_'
    # check length
    if len(my_word2) != len(other_word):
        return False
    for i in range(len(other_word)):
        # print(f'other_word[i] = {other_word[i]} - my_word2[i] = {my_word2[i]}')

        if (other_word[i] != my_word2[i]):
            if (my_word2[i] == '_'):
                if other_word[i] in my_word2:
                    return False
            else:
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    Tests:
        show_possible_matches("t_ _ t")
        show_possible_matches("abbbb_ ")
        show_possible_matches("a_ pl_ ")
    '''

    my_word2 = my_word.replace(" ","")
    list_similar = []

    for word in wordlist:
        if len(word) == len(my_word2):
            cont_valid = 0
            for i in range(len(my_word2)):
                if my_word2[i] != word[i] and my_word2[i] != "_":
                    break
                if my_word2[i] == word[i]:
                    cont_valid += 1
                if my_word2[i] == "_" and word[i] not in my_word2:
                    cont_valid += 1

            if cont_valid == len(word):
                list_similar.append(word)
                # if my_word2[i] == "_" and word[i] not in my_word2:
                #     list_similar.append(word)

    if not list_similar:
        print('No matches found')
    else:
        print(list_similar)





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
