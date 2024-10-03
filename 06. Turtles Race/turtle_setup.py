from turtle import Turtle

# Constants for turtle setup
x_start_position = -230
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

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
