from datetime import datetime

def chat_logger():
    print("=== Mini Chat Logger ===")
    print("Type 'exit' to stop chatting.\n" )

    while True:
        sender = input("Enter sender name (A/B): ")
        if sender.lower() == "exit":
            break

        message = input("Enter massage: ")
        if message.lower() == "exit":
            break

        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")


        output = f"{sender}: {message}| Date : {date} | Time : {time}\n"
        print(output)



        with open ("chat_logger.txt" , "a" , encoding = "utf-8") as file:
         file.write(output)


chat_logger()