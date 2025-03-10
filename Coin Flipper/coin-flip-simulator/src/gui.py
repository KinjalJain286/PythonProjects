from tkinter import Tk, Label, Button, Entry, StringVar, IntVar
import random

class CoinFlipSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Coin Flip Simulator")

        self.result_var = StringVar()
        self.count_heads = IntVar()
        self.count_tails = IntVar()

        self.label = Label(master, text="Enter number of flips:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.flip_button = Button(master, text="Flip Coin", command=self.flip_coins)
        self.flip_button.pack()

        self.result_label = Label(master, textvariable=self.result_var)
        self.result_label.pack()

        self.count_label = Label(master, text="")
        self.count_label.pack()

    def flip_coins(self):
        try:
            num_flips = int(self.entry.get())
            self.count_heads.set(0)
            self.count_tails.set(0)
            results = []

            for _ in range(num_flips):
                result = self.flip_coin()
                results.append(result)
                if result == "Heads":
                    self.count_heads.set(self.count_heads.get() + 1)
                else:
                    self.count_tails.set(self.count_tails.get() + 1)

            self.result_var.set(f"Results: {results}")
            self.count_label.config(text=f"Heads: {self.count_heads.get()}, Tails: {self.count_tails.get()}")

        except ValueError:
            self.result_var.set("Please enter a valid number.")

    @staticmethod
    def flip_coin():
        return "Heads" if random.randint(0, 1) == 0 else "Tails"

if __name__ == "__main__":
    root = Tk()
    simulator = CoinFlipSimulator(root)
    root.mainloop()