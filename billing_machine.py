from datetime import datetime

def billing_system():
    print("=== Simple Billing System ===")
    items = []
    grand_total = 0 


    while True:
      name = input("Enter item name : ")
      qty = int(input("Enter quantity : "))
      price = float(input("Enter price per item: ₹"))


      total = qty*price
      grand_total += total 


      items.append({"name": name , "qty": qty , "price": price , "total": total})

    

      more = input("Add more items? (yes/no):").lower()
      if more != "yes":
        break

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")


    print("\n==== Final Bill ====")
    for item in items:
     print(f"{item['name']} x {item['qty']} @ ₹ {item['price']} = ₹{item['total']}")

    print("----------------------------")
    print(f"Total: ₹{grand_total} ")
    print(f"Date:{date} | Time: {time}")


    with open ("bill.txt", "w", encoding = "utf-8") as file:
          file.write("==== Simple Billing System ====\n")
          for item in items:
             

           file.write(f"{item['name']} x {item['qty']} @ ₹{item['price']} = ₹{item['total']}\n")
          file.write(f"Total: ₹{grand_total}\n")
          file.write(f"Date:{date }| Time : {time}\n")



billing_system()