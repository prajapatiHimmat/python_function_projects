print("Welcome to Multiplicatin Table Generator!\n")

num = int(input("Enter a number to generate its table: "))
print(f"\n Multiplication Table for {num}:\n")

for i in range(1,11):
    result = num*i 
    print(f"{num} x {i} = {result}")


print("\n Table generated successfully! ")