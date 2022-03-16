import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_hangman(tries):
    return f"[Hangman with {tries} attempts remaining]"

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    remaining_tries = 6
    print("Let's play Hangman!")
    print(display_hangman(remaining_tries))
    print(word_completion)
    print("\n")
    while not guessed and remaining_tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter", guess)
            elif guess not in word:
                remaining_tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job;", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                
        elif guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                remaining_tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")

        print(display_hangman(remaining_tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()