# File: /coin-flip-simulator/coin-flip-simulator/src/main.py

import random
from user_input import get_user_input
from coin_flip import flip_coin
from result_counter import ResultCounter
from gui import run_gui

def main():
    print("Welcome to the Coin Flip Simulator!")
    
    # Ask user if they want to use the GUI
    use_gui = input("Would you like to use the graphical interface? (yes/no): ").strip().lower()
    
    if use_gui == 'yes':
        run_gui()
    else:
        result_counter = ResultCounter()
        
        while True:
            num_flips = get_user_input()
            for _ in range(num_flips):
                result = flip_coin()
                result_counter.update(result)
            
            print(f"Heads: {result_counter.heads_count}, Tails: {result_counter.tails_count}")
            print(f"Heads Percentage: {result_counter.get_heads_percentage()}%")
            print(f"Tails Percentage: {result_counter.get_tails_percentage()}%")
            
            repeat = input("Do you want to flip again? (yes/no): ").strip().lower()
            if repeat != 'yes':
                break

if __name__ == "__main__":
    main()