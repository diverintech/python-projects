import random

# Get user bet and validate it
def get_user_bet(screen, colors):
    while True:
        user_bet = screen.textinput(title="Make your bet",
                                    prompt=f"Which turtle will win the race? Choose from {', '.join(colors)}: ")
        if user_bet in colors:
            return user_bet
        print("Invalid color! Please choose a valid color.")

# Start the race
def start_race(turtles, user_bet, x_end_position):
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
