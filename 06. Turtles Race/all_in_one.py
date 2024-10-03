from turtle import Turtle, Screen
import random

# Constants
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen_height = 400
screen_width = 500
x_start_position = -230
x_end_position = 230


# Calculate dynamic Y positions based on number of turtles and screen height
def calculate_y_positions(num_turtles, screen_height):
    spacing = screen_height // (num_turtles + 1)  # Divide space by number of turtles + 1 (for padding)
    y_positions = [(-screen_height // 2 + spacing * (i + 1)) for i in range(num_turtles)]
    return y_positions


# Screen setup
def setup_screen():
    screen = Screen()
    screen.setup(width=screen_width, height=screen_height)
    return screen


# Create turtles based on colors and dynamic positions
def create_turtles(y_positions):
    turtles = []
    for index in range(len(colors)):
        turtle = Turtle(shape="turtle")
        turtle.shapesize(1, 1, 5)
        turtle.penup()
        turtle.color(colors[index])
        turtle.goto(x=x_start_position, y=y_positions[index])
        turtles.append(turtle)
    return turtles


# Get user bet and validate it
def get_user_bet(screen):
    while True:
        user_bet = screen.textinput(title="Make your bet",
                                    prompt=f"Which turtle will win the race? Choose from {', '.join(colors)}: ")
        if user_bet in colors:
            return user_bet
        print("Invalid color! Please choose a valid color.")


# Start the race
def start_race(turtles, user_bet):
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > x_end_position:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                break
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


# Main game function
def main():
    screen = setup_screen()

    # Dynamically calculate Y positions based on number of turtles and screen height
    y_positions = calculate_y_positions(num_turtles=len(colors), screen_height=screen_height)

    turtles = create_turtles(y_positions)
    user_bet = get_user_bet(screen)
    start_race(turtles, user_bet)
    screen.exitonclick()


if __name__ == "__main__":
    main()
