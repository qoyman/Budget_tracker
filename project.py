import datetime

# Initialize data structures
income = 0.0
expenses = {}
expense_history = []

# Function to add income
def add_income():
    global income
    try:
        amount = float(input("Enter the amount of income: "))
        income += amount
        print(f"Income of {amount} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Function to add expense
def add_expense():
    try:
        category = input("Enter the expense category (e.g., groceries, rent): ").strip().lower()
        amount = float(input("Enter the expense amount: "))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        expense_history.append((category, amount, datetime.date.today()))
        print(f"Expense of {amount} added to {category}!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Function to view summary
def view_summary():
    total_expenses = sum(expenses.values())
    print("\n--- Budget Summary ---")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {total_expenses}")
    print("\nExpenses by Category:")
    for category, amount in expenses.items():
        print(f"{category.capitalize()}: {amount}")
    
    if total_expenses > income:
        overspent = total_expenses - income
        print(f"\nYou have overspent by: {overspent}")
    else:
        savings = income - total_expenses
        print(f"\nYou have saved: {savings}")

