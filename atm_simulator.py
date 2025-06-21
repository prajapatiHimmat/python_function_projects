balance = 1000 
def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print(f"current Balance :  ₹ {balance} ")

def deposit():
    global balance 
    amount = float(input("Enter amount to deposit : ₹ "))
    if amount >0:
        balance += amount
        print (f"₹{amount} deposited successfully. ")
    else:
        print("invalid amount.")

def withdraw():
    global balance 
    amount = float(input("Enter amount to withdraw : ₹ "))
    if 0 < amount <= balance :
        balance -= amount 
        print(f"₹{amount} withdrawn successfully. ")
    else: 
        print(" insufficient balance or invalid amount. ")

while True :
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4': 
        print("exiting.... thank you for using our ATM ")

        break
    else :
        print("invalide choice. please try again. ")

