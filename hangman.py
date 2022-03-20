import random
from words import word_list


def get_word():
    """Returns a random word from the global word list"""
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """Triggers a single round of the game"""
    # Initialise the game state
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    remaining_tries = 6

    # Displays introductory text and information
    print("Let's play Hangman!")
    print(display_hangman(remaining_tries))
    print(word_completion)
    print("\n")

    while not guessed and remaining_tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            # The user has guessed a single letter
            if guess in guessed_letters:
                # The letter has already been guessed
                print("You have already guessed the letter", guess)
            elif guess not in word:
                # Incorrect guess
                remaining_tries -= 1
                guessed_letters.append(guess)
            else:
                # Correct guess
                print("Good job;", guess, "is in the word!")
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                # Gets the index of all the letters in `word` that match `letter`
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    # Updates the word_as_list with each new correct guess
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    # The word has been fully guessed
                    guessed = True

        elif guess.isalpha():
            # The user has guessed a word
            if guess in guessed_words:
                # The word has already been guessed
                print("You have already guessed the word", guess)
            elif guess != word:
                # The word is incorrect
                print(guess, "is not the word.")
                remaining_tries -= 1
                guessed_words.append(guess)
            else:
                # The word is correct
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        # Re-display the updated game information
        print(display_hangman(remaining_tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")


def display_hangman(tries):
    """Returns an ascii art hangman that matches the provided number or remaining tries"""
    stages = [  # final state: head, torso, both arms, and both legs
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """,
        # head, torso, both arms, and one leg
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -
                """,
        # head, torso, and both arms
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -
                """,
        # head, torso, and one arm
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        -
        """,
        # head and torso
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        -
        """,
        # head
        """
        --------
        |      |
        |      O
        |    
        |      
        |     
        -
        """,
        # initial empty state
        """
        --------
        |      |
        |      
        |    
        |      
        |     
        -
        """,
    ]
    return stages[tries]


def main():
    play(get_word())

    # Prompt the user to play again after each game
    while input("Play Again? (Y/N) ").upper() == "Y":
        play(get_word())


if __name__ == "__main__":
    main()
