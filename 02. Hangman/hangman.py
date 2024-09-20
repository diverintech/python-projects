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


print(logo)

game_over = False
placeholder = []
lives = len(stages) - 1

while not game_over:
    language = input(
        "Welcome! Please choose a valid language (PT, EN, FR) or type 'exit' to quit: "
    )

    if language.lower() == "exit":
        print("Thank you for using our program. Goodbye!")
        break

    if is_valid_language(language):
        print(f"You have selected {language.upper()}.")

        word_list = import_word_list(language)
        chosen_word = random.choice(word_list)
        chosen_word_length = len(chosen_word)
        chosen_word_list = list(chosen_word)

        for position in range(chosen_word_length):
            placeholder += "_"

        print(f"The word you have to guess is {" ".join(placeholder)}")

        while not game_over:
            guess = input("Guess a letter: ").lower()

            if not chosen_word.__contains__(guess):
                lives -= 1
                print(f"Choose wisely, you lost 1 life and now you have {lives} left")
            else:

                for position in range(chosen_word_length):
                    if chosen_word_list[position] == guess:
                        placeholder[position] = guess
                        print(
                            f"Well done! You hit a letter and keep your {lives} lives"
                        )

            display = " ".join(placeholder)
            print(stages[lives])
            print(f"Word to guess: {display}")

            if "_" not in display:
                game_over = True
                print(
                    f"Congratulations! You've won! The word was '{chosen_word}'. I hope you had fun playing!"
                )
                break
            elif lives == 0:
                game_over = True
                print(f"Oh no! You've lost. The word was '{chosen_word}'.")
                break
