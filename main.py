import random

SEPARATOR = 35 * '='


# Function for better clarity and readability. all other functions are used here
def main():
    word_chars = secret_word()
    play_game(word_chars)
    # Loop that solves if player want to play again
    while True:
        play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
        if play_again == 'y':
            word_chars = secret_word()
            play_game(word_chars)
        elif play_again == 'n':
            print('EXIT...')
            break
        else:
            print('Wrong input.')


# Function which choose random word from txt file and create a list and append every letter in word to it and return
# the list
def secret_word():
    choose_from = []
    letters = []
    with open('words.txt', 'r') as txt:
        txt.readline()
        for word in txt:
            choose_from.append(word)
    random_word = random.choice(choose_from)
    format_random_word = ''.join(random_word.strip('\n'))
    for ch in format_random_word:
        letters.append(ch)
    return letters


hangman_construction = ["""
                --------
                |      |
                |      O
                |    _/|\_
                |      |   
                |    _/ \_
                |
                ---
                """,
                        """
                --------
                |      |
                |      O
                |    _/|\_
                |      |      
                |
                |
                ---
                """,
                        """
                ---------
                |       |
                |       O
                |     _/|\_
                |      
                |
                |
                ---
                """,
                        """
                --------
                |      |
                |      O
                |
                |
                |
                |
                ---
                """,
                        """
                --------
                |      |
                |      
                |
                |
                |
                |
                ---
                """,
                        """
                --------
                |      
                |      
                |
                |
                |
                |
                ---
                """
                        ]


# Function that solves whole game play, word = secret word
def play_game(word):
    print("""Welcome. Let's play HANGMAN. Try to guess the secret word. 
Player have 11 attempts but only 6 hp. 
If player guess right letter he loses 1 attempt. 
If player don't guess right letter he loses 1 attempt and 1 hp. """)
    attempts = 11
    hp = 6
    # For hiding the word. Every letter = - 
    hidden_word = len(word) * '-'
    guessed_letters = []
    print(' '.join(hidden_word))
    # Loop that solves whole gameplay
    while True:
        # Requests input from player(letter) If letter was already use 
        while True:
            guess = input('Type letter: ').lower()
            print(SEPARATOR)
            if guess in guessed_letters:
                print('You already try this letter.')
            else:
                guessed_letters.append(guess)
                break
        attempts -= 1
        hidden_word_as_list = list(hidden_word)
        # Passes all indices and values in the secret word. 
        for i, ch in enumerate(word):
            # If there is a match with guess letter and letter in secret word. 
            # Displays the message and the letter in secret word on the right index.
            if ch == guess:
                print(f'Bravo, {guess} is in the word.', f'{attempts} left | {hp} left', SEPARATOR, sep='\n')
                hidden_word_as_list[i] = guess
            hidden_word = "".join(hidden_word_as_list)
        print(hidden_word)
        print(SEPARATOR)
        # If guessed char is not in secret word. Displays message and hangman construction depends on actual amount
        # of hp.
        if guess not in word:
            hp -= 1
            print('That letter is not in the word.', hangman_construction[hp],
                  f'{attempts} attempts left | {hp} hp left', SEPARATOR, sep='\n')
        # Check the condition  whether the player has won(each letter in secret word is guessed) or 
        # loss(not every letter is guessed before player loses all attempts or hp)
        if '-' not in hidden_word:
            print(SEPARATOR, f'You win! The secret word is {"".join(word)}.', SEPARATOR, sep='\n')
            break
        elif ('-' in hidden_word and attempts == 0) or ('-' in hidden_word and hp == 0):
            print(SEPARATOR, f'You loss! The secret word is {"".join(word)}.', SEPARATOR, sep='\n')
            break


main()
