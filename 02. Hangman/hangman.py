import random

from hangman_art import logo, stages


def is_valid_language(lang):
    return lang.upper() in ["PT", "EN", "FR"]


def import_word_list(lang):
    if lang.upper() == "EN":
        from hangman_words_en import word_list
    elif lang.upper() == "FR":
        from hangman_words_fr import word_list
    elif lang.upper() == "PT":
        from hangman_words_pt import word_list
    return word_list


def initialize_game():
    print(logo)
    while True:
        language = input(
            "Please choose a valid language (PT, EN, FR) or type 'exit' to quit: "
        ).lower()
        if language.lower() == "exit":
            print("Thank you for playing! Goodbye!")
            return None
        if is_valid_language(language):
            print(f"You have selected {language.upper()}.")
            return import_word_list(language)
        else:
            print("Invalid language choice. Please try again.")


def play_game(chosen_word):
    placeholder = ["_"] * len(chosen_word)
    lives = len(stages) - 1
    guessed_letters = set()

    while lives > 0 and "_" in placeholder:
        print(stages[lives])
        print(f"Word to guess: {' '.join(placeholder)}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    placeholder[index] = guess
            print(f"Good job! You guessed a letter.")
        else:
            lives -= 1
            print(f"Incorrect guess. You have {lives} lives remaining.")

    if "_" not in placeholder:
        print(f"Congratulations! You've won! The word was '{chosen_word}'.")
    else:
        print(stages[lives])
        print(f"Game over. The word was '{chosen_word}'.")


def main():
    while True:
        word_list = initialize_game()
        if word_list is None:
            break

        chosen_word = random.choice(word_list)
        play_game(chosen_word)

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
