# Coin Flip Simulator

This project is a simple coin flip simulator that allows users to simulate flipping a coin multiple times. It incorporates randomization, user input for the number of tosses, result counting, and an optional graphical representation using tkinter.

## Features

- Simulates flipping a coin with random outcomes of "Heads" or "Tails".
- Allows users to specify the number of flips.
- Counts the results of each flip and calculates the percentage of "Heads" and "Tails".
- Provides a command-line interface for interaction.
- Includes an optional graphical user interface (GUI) for a more visual experience.

## Files

- `src/main.py`: Entry point of the application that initializes the program and handles user input.
- `src/coin_flip.py`: Contains the function to simulate a single coin toss.
- `src/user_input.py`: Manages user input for the number of flips and session repetition.
- `src/result_counter.py`: Class that tracks and calculates the results of the coin flips.
- `src/gui.py`: Implements a GUI using tkinter for visual representation of results.

## Requirements

To run this project, you need to install the following dependencies:

- Python 3.x
- tkinter (usually included with Python installations)

You can install any additional required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Program

To run the coin flip simulator, execute the following command in your terminal:

```
python src/main.py
```

Follow the prompts to enter the number of flips and view the results. If you choose to use the GUI, you can run the `gui.py` file directly.

## License

This project is open-source and available for modification and distribution.