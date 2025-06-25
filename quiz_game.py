score = 0 
print("Welcome to the Quiz game!\n")

print("1. What is the capital of india ? ")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
print("d) Chennai")
ans = input("Your answer: ").lower()

if ans == 'b':
    print("Correct!")
    score += 1

else:
    print("Wrong! Correct answer is: b) Delhi")


print("\n2. Which planet is known as the red planet ?")
print("a) Earth")
print("b) Venus")
print("c) Mars")
print("d) Jupiter")
ans = input("Your answer: ").lower()

if ans == 'c':
    print("Correct!")
    score += 1

else:
    print("Wrong! Correct answer is: c) Mars")



print("\n3. Who wrote the ramayana ? ")
print("a) Valmiki")
print("b) Tulsidas")
print("c) Ved Vyas")
print("d) Kalidas")
ans = input("Your answer: ").lower()

if ans == 'a':
    print("Correct!")
    score += 1

else:
    print("Wrong! Correct answer is: a) Valmiki")




print("\n4. What is the value of pi ? ")
print("a) 2.12")
print("b) 3.14")
print("c) 1.41")
print("d) 4.13")
ans = input("Your answer: ").lower()

if ans == 'b':
    print("Correct!")
    score += 1

else:
    print("Wrong! Correct answer is: b) 3.14")





print("\n5. Which language is used to write python ? ")
print("a) English")
print("b) C")
print("c) Java")
print("d) Python")
ans = input("Your answer: ").lower()

if ans == 'd':
    print("Correct!")
    score += 1

else:
    print("Wrong! Correct answer is: d) Python")




print("\n Your final score is:" , score, "/ 5")

if score == 5 :
    print("Excellent !")
elif score >= 3:
    print("good job !")
else:
    print("Try Again ! ")



