todo_list = []
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print ("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. REMOVE TASK")
    print("4. EXIT")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter Task To Add:")
        todo_list.append(task)
        print(f"Task Added  : {task}")

    elif choice == '2':
        if len(todo_list) == 0 :
            print("No Tasks Found. ")
        else: 
            print("\n Your Tasks. ")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}.{task}")

    elif choice == '3':
        if len(todo_list) == 0:
            print("No Tasks To Remove. ")

        else :
           for i , task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

        task_num = int(input("Enter Task Number To Remove : "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task Removed: {removed}" )

        else :
            print("Invalid Task Number.")

    elif choice == '4':
        print("Exiting... Have A Nice Day !")

        break 

    else:
        print("Invalid Choice. Please Try Again.")
