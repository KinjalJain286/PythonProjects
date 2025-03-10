class ResultCounter:
    def __init__(self):
        self.heads_count = 0
        self.tails_count = 0

    def update_counts(self, result):
        if result == "Heads":
            self.heads_count += 1
        elif result == "Tails":
            self.tails_count += 1

    def get_counts(self):
        return self.heads_count, self.tails_count

    def calculate_percentages(self):
        total_flips = self.heads_count + self.tails_count
        if total_flips == 0:
            return 0, 0
        heads_percentage = (self.heads_count / total_flips) * 100
        tails_percentage = (self.tails_count / total_flips) * 100
        return heads_percentage, tails_percentage