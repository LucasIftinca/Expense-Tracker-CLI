import os
from src.storage import Storage
from src.ui import ExpenseTrackerUI

# Constants
DATA_FILE = os.path.join("data", "expenses.csv")

def main():
    """
    Entry point of the application.
    Initializes the storage and UI components, then starts the main loop.
    """
    # Initialize Storage with the path to the CSV file
    storage = Storage(DATA_FILE)

    # Initialize UI and inject the storage dependency
    app = ExpenseTrackerUI(storage)

    # Run the application
    app.run()

if __name__ == "__main__":
    main()