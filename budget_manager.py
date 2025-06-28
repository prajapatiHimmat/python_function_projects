from datetime import datetime

def budget_manager():
    balance = 0
    while True:

        print("\n=== Mini Budget Manager ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice (1/4) : ")

        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")


        if choice == '1':
           income = float(input("Enter Income amount: ₹"))
           balance += income
           with open("budget_log.txt" , "a" , encoding="utf-8") as file:
                file.write(f"[{date_time}] +₹{income} (income)\n")


        elif choice == '2':
            expense = float(input("Enter expense amount: ₹"))
            category = input("Enter expense catagory: ")
            balance -= expense
            with open("budget_log.txt" , "a" , encoding="utf-8") as file:
                 file.write(f"[{date_time}] -₹{expense} ({category})\n")


        elif choice == '3':
            print("\n--- Budget Summary ---")
            try:
               with open("budget_log.txt" , "r" , encoding="utf-8") as file:
                    print(file.read())
               print(f"Current Balance : ₹{balance}")
            except FileNotFoundError:
                print("No data found yet !")
    
        elif choice== '4':
         print("Exiting Budget Manager. Goodbye !")


         break


        else :
          print("Invalid chioce. try again ! ")



budget_manager()
