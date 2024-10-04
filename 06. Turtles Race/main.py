from screen_setup import setup_screen
from turtle_setup import create_turtles, colors
from race import get_user_bet, start_race
from utils import calculate_y_positions  # Import from utils

# Constants
screen_height = 400
x_end_position = 230


def main():
    screen = setup_screen()

    # Dynamically calculate Y positions based on number of turtles and screen height
    y_positions = calculate_y_positions(num_turtles=len(colors), screen_height=screen_height)

    turtles = create_turtles(y_positions)
    user_bet = get_user_bet(screen, colors)

    if user_bet is not None:
        start_race(turtles, user_bet, x_end_position)
        screen.exitonclick()
    else:
        screen.bye()

if __name__ == "__main__":
    main()
