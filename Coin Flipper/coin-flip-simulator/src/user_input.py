def get_number_of_flips():
    while True:
        try:
            flips = int(input("Enter the number of coin flips: "))
            if flips > 0:
                return flips
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def ask_to_repeat():
    while True:
        repeat = input("Do you want to flip again? (yes/no): ").strip().lower()
        if repeat in ['yes', 'y']:
            return True
        elif repeat in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")