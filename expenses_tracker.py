expenses = []

def add_expense(category , amount):
    expenses.append({"category": category ,"amount": amount})
    print(f"added {amount} in {category} category.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\n--- Expense Summary ---") 
        for e in expenses:
            print(f"{e['category']} - ₹{e['amount']}")

while True:
    print("\n---- Expense Tracker ----")
    print("1. add expense")
    print("2. view expenses")
    print("3. exit")
    choice = input("Enter your choice : ")

    if choice == '1':
        category = input("Enter category :")
        amount = float(input("Enter amount : "))
        add_expense(category, amount)

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        print("Exiting... Goodbye! ")
        break
    else:
        print("Invalid choice. try again.")
    
    again = input("\n want to continue? (yes/no) :")
    if again.lower() != 'yes':
        break

