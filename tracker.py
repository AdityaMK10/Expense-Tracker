import csv
from datetime import datetime

file_name = "Expense_tracker.csv"


def expense_tracker():

    amount = float(input("Enter the amount that you have spent:"))
    category = input("Enter the category in which you have spent it on:")
    description = input("enter a description:")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense_list = [timestamp, amount,category,description]

    with open(file_name,mode = 'a' , newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Timestamp", "Amount", "Category", "Description"])

        writer.writerow(expense_list)

    print("Expense recorded successfully")
    print("-------------------------------------------")


def total_expenses():
    category_totals = {}
    with open("Expense_tracker.csv",mode='r') as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            timestamp, amount, category, description = row
            amount = float(amount)
            category = category.title()
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    for category, total in category_totals.items():
        print(f"{category}: ₹ {total:.2f}")
def main():

    while True:
        print("\nExpense Tracker")
        print("1. Add a new expense")
        print("2. Display total expenses category-wise")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            expense_tracker()
        elif choice == '2':
            total_expenses()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()






