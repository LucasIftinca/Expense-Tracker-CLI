class Transaction:
    def __init__(self, date: str, category: str, amount: float, description: str):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_list(self):
        """Converts the object to a list for CSV storage."""
        return [self.date, self.category, self.amount, self.description]

    def __str__(self):
        """String representation for printing."""
        return f"{self.date} | {self.category} | {self.amount:.2f} RON | {self.description}"