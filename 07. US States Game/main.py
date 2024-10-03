import turtle
import pandas
import difflib

# Files
us_map = "blank_states_img.gif"
states_list = "50_states.csv"
# Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(us_map)
turtle.shape(us_map)

# Grab all the data from the csv file
data_states = pandas.read_csv(states_list)
# Store only the states names in a list
all_states = data_states.state.to_list()
# Empty list to store the guessed states
guessed_states = []

def get_user_answer():
    feedback = ""  # Variable to store feedback messages

    while len(guessed_states) < 50:
        # Display feedback and prompt user for the next guess
        prompt = (f"{feedback}\n\nGuess a state name:" if feedback else "Guess a state name:")

        user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt=prompt)

        # Check if the user pressed 'Cancel'
        if user_answer is None:
            print("Game exited by user.")
            return  # Exit the function if the user cancels the input

        user_answer = user_answer.title()

        if user_answer in guessed_states:
            feedback = f"You've already guessed {user_answer}!"
        elif user_answer in all_states:
            guessed_states.append(user_answer)
            feedback = f"Well Done! You guessed {user_answer}!"
        elif get_closest_state(user_answer):
            closest_state = get_closest_state(user_answer)
            confirm = screen.textinput(title="Did you mean this?", prompt=f"Did you mean {closest_state}? (yes/no)").lower()
            if confirm == "yes" and closest_state not in guessed_states:
                guessed_states.append(closest_state)
                feedback = f"Well Done! You guessed {closest_state}!"
            else:
                feedback = "Try again."
        else:
            feedback = "Incorrect guess, try again."

    # Display final message
    screen.textinput(title="Congratulations!", prompt="You've guessed all 50 states! Press OK to exit.")

def get_closest_state(user_answer):
    closest_match = difflib.get_close_matches(user_answer, all_states, n=1, cutoff=0.6)
    if closest_match:
        return closest_match[0]
    return None

# Main
get_user_answer()
