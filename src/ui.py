import os
from typing import List
from .models import Transaction
from .storage import Storage
from .ai_agent import AIAgent

class ExpenseTrackerUI:
    def __init__(self, storage: Storage):
        self.storage = storage
        # Citim cheia API din variabila de mediu (pentru siguranță)
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            self.ai_agent = AIAgent(api_key)
        else:
            self.ai_agent = None

    def display_menu(self):
        print("\n=== 💸 Expense Tracker CLI (AI Powered) ===")
        print("1. Add Expense (Manual)")
        print("2. ✨ Smart Add (AI Magic)")
        print("3. View All Expenses")
        print("4. Show Summary")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nSelect option: ").strip()

            if choice == '1':
                self.add_expense_manual()
            elif choice == '2':
                self.add_expense_ai()
            elif choice == '3':
                self.view_expenses()
            elif choice == '4':
                self.show_summary()
            elif choice == '5':
                print("Bye! 👋")
                break
            else:
                print("Invalid option.")

    def add_expense_manual(self):
        try:
            print("\n--- Manual Entry ---")
            date = input("Date (YYYY-MM-DD): ")
            cat = input("Category: ")
            amt = float(input("Amount: "))
            desc = input("Description: ")
            self.storage.save_transaction(Transaction(date, cat, amt, desc))
            print("✅ Saved!")
        except ValueError:
            print("❌ Invalid number.")

    def add_expense_ai(self):
        if not self.ai_agent:
            print("\n⚠️  GEMINI_API_KEY not found! Please set it in your terminal.")
            print("Run: export GEMINI_API_KEY='your_key_here'")
            return

        print("\n--- ✨ Smart Entry ---")
        print("Tell me what you bought (e.g., 'I spent 50 lei on Taxi today')")
        user_input = input("> ")
        
        print("🤖 Thinking...")
        transaction = self.ai_agent.parse_expense(user_input)
        
        if transaction:
            print(f"\nI understood:\n{transaction}")
            confirm = input("Save this? (y/n): ").lower()
            if confirm == 'y':
                self.storage.save_transaction(transaction)
                print("✅ Saved!")
            else:
                print("❌ Cancelled.")
        else:
            print("Sorry, I couldn't understand that.")

    def view_expenses(self):
        txs = self.storage.load_transactions()
        print(f"\n{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
        print("-" * 60)
        for t in txs:
            print(f"{t.date:<12} | {t.category:<15} | {t.amount:<10.2f} | {t.description}")

    def show_summary(self):
        txs = self.storage.load_transactions()
        summary = {}
        for t in txs:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        print("\n--- Summary ---")
        for c, a in summary.items():
            print(f"{c:<15}: {a:.2f} RON")