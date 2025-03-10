import random

def coin_flip():
    return random.choice(["Heads", "Tails"])

def multiple_flips(num_flips):
    results = {"Heads": 0, "Tails": 0}
    for _ in range(num_flips):
        result = coin_flip()
        results[result] += 1
    return results

def display_results(results, num_flips):
    heads_count = results["Heads"]
    tails_count = results["Tails"]
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    print(f"\nResults after {num_flips} flips:")
    print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")

def main():
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips < 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        results = multiple_flips(num_flips)
        display_results(results, num_flips)

        repeat = input("Do you want to flip again? (yes/no): ").strip().lower()
        if repeat != "yes":
            break

if __name__ == "__main__":
    main()