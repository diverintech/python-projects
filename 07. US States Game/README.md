
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

## How to Set Up the Project in PyCharm

1. **Download and Install PyCharm**: If you haven't already, download and install [PyCharm](https://www.jetbrains.com/pycharm/download/).

2. **Create a New Project**:
   - Open PyCharm and create a new project by navigating to **File** > **New Project**.
   - Choose a location for the project and select the option to create a new virtual environment (**Virtualenv**).

3. **Install Required Packages**:
   - Open the terminal in PyCharm and run the following commands to install the necessary packages:
     ```bash
     pip install pandas
     ```
   - The `turtle` package comes with Python, but if you encounter errors, you may need to configure your environment to support it.

4. **Add Required Files**:
   - Ensure that the following files are in your project directory:
     - `50_states.csv`: This CSV file should contain the list of U.S. states with corresponding coordinates for displaying them on the map.
     - `blank_states_img.gif`: This is the map of the United States that will be displayed in the game.

5. **Run the Game**:
   - After setting up everything, open the `main.py` file and click **Run** to start the game.
   - The game window will open, displaying the U.S. map. You will be prompted to guess the names of states.

6. **Game Instructions**:
   - The goal of the game is to guess all 50 states.
   - Enter the name of a state when prompted. If the state is correct, its name will be displayed on the map.
   - If your guess is incorrect, the game may suggest a similar state name to help you.
   - When you finish, states you missed will be saved in `states_to_learn.csv`, and states you've guessed correctly will be saved in `guessed_states.csv`.

## Project Structure

Ensure that the project folder contains the following files:

```
U.S. States Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── guessed_states.csv (generated after playing the game)
└── states_to_learn.csv (generated after playing the game)
```

## How to Play

1. Run the game by executing `main.py` in PyCharm.
2. Enter the name of a U.S. state when prompted.
3. The game will give feedback on your guess. Keep guessing until you've identified all 50 states.
4. At the end of the game, review the `states_to_learn.csv` file to see which states you missed.

## License

This project is for educational purposes and is open to modification and use as needed.
