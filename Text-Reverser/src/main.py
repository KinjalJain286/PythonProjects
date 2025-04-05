# main.py

import sys
from menu import display_menu
from reverser import reverse_character_order, reverse_word_order

def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            text = input("Enter the text to reverse character order: ")
            reversed_text = reverse_character_order(text)
            print(f"Reversed Character Order: {reversed_text}")
        
        elif choice == '2':
            text = input("Enter the text to reverse word order: ")
            reversed_text = reverse_word_order(text)
            print(f"Reversed Word Order: {reversed_text}")
        
        elif choice == '3':
            text = input("Enter the text to save to file: ")
            filename = input("Enter the filename (with .txt extension): ")
            from utils.file_operations import save_to_file
            save_to_file(text, filename)
            print(f"Text saved to {filename}.")
        
        elif choice == '4':
            print("Exiting the program.")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()