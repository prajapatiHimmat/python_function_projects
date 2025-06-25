import random
import time

print("Welcome to mental math trainer with timer!\n")
score = 0 

for i in range(1,6):
    num1 = random.randint(1,30)
    num2 = random.randint(1,30)
    operation = random.choice(['+' , '-' , '*'])

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1- num2
    else: 
        correct_answer = num1 * num2 


    print(f"Q{i}: What is {num1} {operation } {num2}? ")
    print("you have 10 seconds to answer!")

    start_time = time.time()

    try :
     user_ans = int(input("Your answer: "))
    except: 
     user_ans = None

    end_time = time.time()
    time_taken = end_time - start_time

    if time_taken > 10:
     print(f" Time`s up ! you took {round(time_taken , 2)} seconds.")
     print(f" Correct answer was : { correct_answer}\n")
    elif user_ans == correct_answer:
      print("correct!\n")
      score += 1
    else :
      print(f" wrong ! correct answer was : {correct_answer}\n")

print(" Game Over!")
print(f"Your final score : {score}/5")


if score == 5:
    print("genius level!")
elif score >= 3:
    print("good job!")
else:
    print("keep practicing! ")