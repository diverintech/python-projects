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
            save_unlearned_states()  # Save states the user didn't guess
            save_guessed_states()  # Save states the user guessed
            return  # Exit the function if the user cancels the input

        user_answer = user_answer.title()

        if user_answer in guessed_states:
            feedback = f"You've already guessed {user_answer}!"
        elif user_answer in all_states:
            guessed_states.append(user_answer)
            feedback = "Well Done!"
            display_state_on_map(user_answer)  # Call function to display the state on the map
        elif get_closest_state(user_answer):
            closest_state = get_closest_state(user_answer)
            confirm = screen.textinput(title="Did you mean this?", prompt=f"Did you mean {closest_state}? (yes/no)").lower()

            if confirm == "yes":
                if closest_state in guessed_states:
                    feedback = f"You've already guessed {closest_state}!"  # Feedback caso o estado já tenha sido adivinhado
                else:
                    guessed_states.append(closest_state)
                    feedback = "Well Done!"
                    display_state_on_map(closest_state)  # Exibe o estado no mapa
            else:
                feedback = "Try again."

        else:
            feedback = "Incorrect guess, try again."

    # Display final message
    screen.textinput(title="Congratulations!", prompt="You've guessed all 50 states! Press OK to exit.")
    save_unlearned_states()  # Save states the user didn't guess
    save_guessed_states()  # Save states the user guessed

def get_closest_state(user_answer):
    closest_match = difflib.get_close_matches(user_answer, all_states, n=1, cutoff=0.6)
    if closest_match:
        return closest_match[0]
    return None

# New function to display the guessed state on the map
def display_state_on_map(state_name):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data_states[data_states.state == state_name]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_name)

# Function to save unlearned states to a CSV file
def save_unlearned_states():
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states, columns=["State"])
    new_data.to_csv("states_to_learn.csv", index=False)
    print("States to learn saved to states_to_learn.csv")

# Function to save guessed states to a CSV file
def save_guessed_states():
    guessed_data = pandas.DataFrame(guessed_states, columns=["State"])
    guessed_data.to_csv("guessed_states.csv", index=False)
    print("Guessed states saved to guessed_states.csv")

# Main
get_user_answer()
