US States Game

This is a Python script that helps you learn and guess the states of the United States. It uses the Turtle graphics library and the Pandas library to create an interactive game.
How it Works

    The script imports the necessary modules and libraries, including Turtle and Pandas.
    It sets up the game screen and loads a blank map of the US as the background.
    The script reads a CSV file containing the names, coordinates, and other data for all 50 US states.
    The game loop starts, and the user is prompted to enter the name of a state. The user can also type "Exit" to finish the game.
    If the user enters a valid state name, the script will place a turtle at the correct location on the map and write the state name.
    The correct guesses are stored in a list, and the game continues until all 50 states have been guessed.
    If the user types "Exit", the script will create a new CSV file called "states_to_learn.csv" containing the names of the states that the user failed to guess.

Requirements

    Python 3.x
    Turtle graphics library
    Pandas library
    A CSV file containing the 50 US states data (included in the repository)
    A blank map of the US (included in the repository)

Usage

    Clone or download the repository to your local machine.
    Open a Python environment and navigate to the project directory.
    Run the script using the command python us_states_game.py.
    Follow the on-screen prompts to guess the states.
    When you're done, the "states_to_learn.csv" file will be created, containing the names of the states you failed to guess.
