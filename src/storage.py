import csv
import os
from typing import List
from .models import Transaction

class Storage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Creates the CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["date", "category", "amount", "description"])

    def save_transaction(self, transaction: Transaction):
        """Appends a new transaction to the CSV file."""
        with open(self.file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(transaction.to_list())

    def load_transactions(self) -> List[Transaction]:
        """Reads all transactions from the CSV file."""
        transactions = []
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions.append(Transaction(
                        date=row["date"],
                        category=row["category"],
                        amount=float(row["amount"]),
                        description=row["description"]
                    ))
        except FileNotFoundError:
            pass
        return transactions