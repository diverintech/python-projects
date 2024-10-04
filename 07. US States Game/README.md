# U.S. States Game

## Description

The U.S. States Game is an interactive Python game where players can test their knowledge of U.S. state names. The game displays a map of the United States and prompts the player to guess the names of all 50 states. When a correct state is guessed, its name is displayed on the map. The game also offers suggestions for close matches when the player makes a typo.

## Features

- **State Guessing**: Players are prompted to guess the name of a U.S. state.
- **Feedback and Suggestions**: If the guess is incorrect, the game suggests the closest state name.
- **Progress Tracking**: Correct guesses are tracked, and states that have not been guessed are saved for review in a CSV file.
- **Map Visualization**: Correct guesses are marked on a U.S. map using the Turtle graphics module.

## Technologies Used

- **Python**: Core programming language.
- **Turtle Graphics**: Used to display the map and write state names on it.
- **Pandas**: Handles data manipulation for the list of states and tracking guesses.
- **Difflib**: Provides close matches for incorrect guesses.

## Prerequisites

- Python 3.x installed on your machine.
- PyCharm IDE (optional but recommended).
- Required Python packages:
  - `pandas`
  - `turtle` (this comes with Python but may need additional configuration in some environments).

## Problem and Solution for Running the Project in Visual Studio Code

If you are facing issues running the project on VS Code, add the following lines to your `settings.json` file:

```json
"python.envFile": "${workspaceFolder}/.env",
"python.terminal.executeInFileDir": true


## How to Play

1. Run the game by executing `main.py` in PyCharm.
2. Enter the name of a U.S. state when prompted.
3. The game will give feedback on your guess. Keep guessing until you've identified all 50 states.
4. At the end of the game, review the `states_to_learn.csv` file to see which states you missed.

## License

This project is for educational purposes and is open to modification and use as needed.
```
