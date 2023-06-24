import random
import string

words = ['lion', 'tiger', 'dog', 'cat', 'cow', 'zebera', 'girraf', 'monkey', 'elephant', 'bear', 'panda', 'leopard', 'jackal']

def select_word(words_list):
    """Select a random word from the list."""
    ch = random.choice(words_list)

    '''if(ch == 'lion'):
        print('King of the Jungle')
    elif(ch == 'tiger'):
        print('National Animal of India')
    elif(ch == 'dog'):
        print('Man\'s best friend')
    elif(ch == 'cat'):
        print('A pet animal')
    elif(ch == 'cow'):
        print('A milk giving animal')
    elif(ch == 'zebera'):
        print('A white/black stripes animal')
    elif(ch == 'girraf'):
        print('A tall animal')
    elif(ch == 'monkey'):
        print('A naughty animal')
    elif(ch == 'elephant'):
        print('A big animal')
    elif(ch == 'bear'):
        print('A wild animal')
    elif(ch == 'panda'):
        print('A cute animal')
    elif(ch == 'leopard'):
        print('A wild animal')
    elif(ch == 'jackal'):
        print('A wild animal')'''
    return ch

def play_hangman(word):
    """Play the hangman game."""
    guessed_letters = set()
    remaining_attempts = 6

    while True:
        print("\nWord: " + " ".join([c if c in guessed_letters else '_' for c in word]))
        print("Attempts remaining: " + str(remaining_attempts))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print("\nCongratulations! You guessed the word: " + word)
                break
        else:
            print("Incorrect guess.")
            remaining_attempts -= 1
            if remaining_attempts == 0:
                print("\nGame over. You ran out of attempts. The word was: " + word)
                break

def main():
    """Main function to run the hangman game."""
    print("Welcome to Hangman! \n")
    print("""Let me introduce you to the game :: \n 
          1. You have to guess the name of the animal.
          2. You have 6 attempts to guess the name of the animal.
          3. You can guess only one letter at a time.
          4. If you guess the letter correctly, it will be displayed.
          5. If you guess the letter incorrectly, you will lose one attempt.
          6. If you guess the name of the animal correctly, you will win the game.
          7. If you guess the name of the animal incorrectly, you will lose the game.\n""")
    print('Guess an animal name :: \n')
    word = select_word(words)
    play_hangman(word)

if __name__ == '__main__':
    main()
