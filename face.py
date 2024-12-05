class BudgetTracker:
    def __init__(self, budget):  
        self.budget = budget
        self.expenses = []

    def add_expense(self, amount, description):
        if amount <= 0:
            print("Expense amount must be positive.")
            return
        if self.get_total_expenses() + amount > self.budget:
            print("Cannot add expense. This will exceed your budget.")
            return
        self.expenses.append({'amount': amount, 'description': description})
        print(f"Added expense: {description} - ${amount:.2f}")

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_remaining_budget(self):
        return self.budget - self.get_total_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense['description']}: ${expense['amount']:.2f}")
        print(f"Total Expenses: ${self.get_total_expenses():.2f}")
        print(f"Remaining Budget: ${self.get_remaining_budget():.2f}\n")


def main():
    print("Welcome to the Budget Tracker!")
    budget = float(input("Enter your budget: "))
    tracker = BudgetTracker(budget)

    while True:
        print("Options:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__": 
    main()
