from datetime import datetime
def medicine_reminder():
   
    while True:
        print("\n=== Medicine Reminder ===")
        print("1. Add New Madicine Reminder ")
        print("2. View all reminders ")
        print("3. check medicine for current time ")
        print("4. exit")

        choice = input("Enter your choice (1/4): ")
     
        if choice == '1':
         med_name = input("Enter Medicine name : ")
         med_time = input("Enter Medicine time (HH:mM): ")
        
         with open ("medicine_reminders.txt" , "a" , encoding = "utf-8" ) as file :
          file.write(f"{med_name},{med_time}\n")
          print("Medicine reminder saved !")


        elif choice == '2':
          print("--- ALL Reminders ---")
          try:
             with open ("medicine_reminders.txt" , "r" , encoding = "utf-8" ) as file:
               print(file.read())
             print("this is a all reminder to get medicine ")
          except FileNotFoundError:
             print("NO data found ! try again. ")


        elif choice == '3':
          now = datetime.now().strftime("%H:%M")
          try:
            with open("medicine_reminders.txt" , "r" , encoding= "utf-8") as file:
              lines = file.readlines()
              found = False
              for line in lines:
                name, time = line.strip().split(",")
                if time == now:
                  print(f"Take your medicine - {name}") 
                  found = True
              if not found :
                print("No medicine for current time.")
          except FileNotFoundError:
            print("No data to check. ")
    
        elif choice == '4':
          print("Exiting... have good day !")

          break 

        else:
         print("Invald choice. try again ! ")


medicine_reminder()
