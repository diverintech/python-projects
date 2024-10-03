# U.S. States Game

## Description

The U.S. States Game is an interactive game written in Python where players can test their knowledge of the states of the United States. Players must guess the name of each state, and the game provides feedback on their answers, suggesting corrections when necessary. The goal is to guess all 50 states.

## Technologies Used

- Python
- Turtle Graphics
- Pandas
- Difflib

## Features

- **State Guessing**: Players enter the name of a state and receive feedback.
- **Suggestions**: If the input is incorrect, the game suggests the closest state.
- **Tracking Correct and Incorrect Guesses**: Correctly guessed states are stored in one file, while unguessed states are saved in another CSV file for future review.
- **Map Visualization**: When a state is correctly guessed, the game marks the state's position on a map using Turtle graphics.

## How to Play

1. Run the `main.py` file to start the game.
2. Enter the name of a state when prompted.
3. Receive feedback on your answer and continue guessing until you guess all 50 states.
4. After finishing, you can review the states you didn't guess correctly in the `states_to_learn.csv` file.
