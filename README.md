# 💸 Expense Tracker CLI

> A robust, terminal-based application for managing personal finances. Built with **Python**, utilizing **Object-Oriented Programming (OOP)** principles and **CSV persistence** for data reliability.

---

## 📖 Overview
This application allows users to track their daily expenses directly from the command line. Unlike simple scripts, this project is architected with scalability in mind, using distinct classes for transactions, file handling, and user interaction.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Data Storage:** CSV (Comma Separated Values)
- **Paradigm:** OOP (Classes, Inheritance, Encapsulation)

## ✨ Key Features
- **Add Expenses:** Record transactions with categories, amounts, and descriptions.
- **View History:** Display a formatted table of all past expenses.
- **Data Persistence:** Automatically saves data to `expenses.csv` so records aren't lost on exit.
- **Summary Statistics:** Calculates total spent per category (e.g., Food, Transport).

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone [https://github.com/LucasIftinca/Expense-Tracker-CLI.git](https://github.com/LucasIftinca/Expense-Tracker-CLI.git)
   cd Expense-Tracker-CLI
   ```

2. **Run the application**
   ```bash
   python main.py
   # OR
   python3 main.py
   ```

## 📂 Project Structure
```text
Expense-Tracker-CLI/
├── data/
│   └── expenses.csv    # Data storage
├── src/
│   ├── models.py       # Transaction class definitions
│   ├── storage.py      # CSV handling logic
│   └── ui.py           # CLI interface logic
├── main.py             # Entry point
└── README.md
```

---
**Author:** Lucas-Ștefan Iftinca