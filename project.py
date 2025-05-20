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

