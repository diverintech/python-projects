from turtle import Screen

# Constants for screen
screen_height = 400
screen_width = 500

def setup_screen():
    screen = Screen()
    screen.setup(width=screen_width, height=screen_height)
    return screen
