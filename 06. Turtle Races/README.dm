# Turtle Race Game

This project features a simple turtle racing game implemented in Python using the Turtle graphics library.

## Project Structure

### 1. `all_in_one.py`
- This file contains the complete implementation of the turtle race in a single script.
- It combines the setup, logic, and user interactions in one place, which can make it easier for quick testing and understanding the flow but can become unwieldy as complexity increases.

### 2. Modular Files
- The modular version consists of multiple files:
  - **`screen_setup.py`**: Handles the setup of the Turtle graphics screen.
  - **`turtle_setup.py`**: Responsible for creating turtles and setting their initial positions.
  - **`race.py`**: Contains the race logic and user betting functionality.
  - **`utils.py`**: Includes utility functions like `calculate_y_positions` for dynamic positioning of turtles.
  - **`main.py`**: The main entry point that ties everything together, calling functions from the other modules.

## Advantages of Modular Approach
- **Maintainability**: Each component can be updated or debugged independently, making the code easier to maintain.
- **Reusability**: Common functions, like positioning turtles, can be reused across different projects or modules.
- **Readability**: Separating functionality into different files makes it easier to read and understand the code structure.

## Choosing the Right Approach
- For small projects or quick prototypes, using a single file can simplify the process.
- As the project grows, breaking it into modular components improves organization and makes future enhancements more manageable.

## Turtle Library Documentation
For more information on the Turtle library, visit the official documentation [here](https://docs.python.org/3/library/turtle.html#module-turtle).
