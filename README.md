# 💸 Smart Expense Tracker CLI (AI-Powered)

> A high-performance terminal application for personal finance management, now supercharged with **Google Gemini 2.0 AI** to process expenses from natural language.

---

## 📖 Overview
This is not just another expense script. This project demonstrates how to bridge the gap between structured data and natural language. It allows users to log expenses manually or simply describe them in plain text (e.g., *"I spent 50 RON on sushi today"*).

## 🚀 Key Features
- **✨ AI Smart Add:** Uses **Gemini 2.0 Flash** to parse dates, amounts, categories, and descriptions from unstructured text.
- **💾 CSV Persistence:** All data is stored locally in `data/expenses.csv`, ensuring your records are permanent.
- **📊 Quick Summary:** Get instant insights into your spending habits by category.
- **🛠️ Modular Architecture:** Built using SOLID principles and Object-Oriented Programming (OOP).

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **AI Integration:** Google GenAI SDK (Gemini 2.0 Flash)
- **Data Storage:** CSV

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/LucasIftinca/Expense-Tracker-CLI.git](https://github.com/LucasIftinca/Expense-Tracker-CLI.git)
   cd Expense-Tracker-CLI
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API Key**
   Get your free API key from [Google AI Studio](https://aistudio.google.com/) and set it as an environment variable:
   ```bash
   export GEMINI_API_KEY='your_secret_key_here'
   ```

5. **Run the app**
   ```bash
   python main.py
   ```

## 📂 Project Structure
```text
Expense-Tracker-CLI/
├── data/
│   └── expenses.csv    # Your persistent data
├── src/
│   ├── models.py       # Data structures (Transaction class)
│   ├── storage.py      # File I/O logic
│   ├── ai_agent.py     # Gemini AI integration logic
│   └── ui.py           # Command-line interface
├── main.py             # App entry point
└── requirements.txt    # Project dependencies
```

---
**Author:** Lucas-Ștefan Iftinca