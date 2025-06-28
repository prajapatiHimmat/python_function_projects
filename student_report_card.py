def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total , max_total):
    return (total/ max_total) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 75:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 45:
        return 'C'
    else:
        return 'fail'
    
while True:
    name = input("Enter student name :")
    sub1 = int(input("Enter marks for subject 1 : "))
    sub2 = int(input("Enter marks for subject 2 : "))
    sub3 = int(input("Enter marks for subject 3 : "))


    marks = [sub1,sub2,sub3]
    total = calculate_total([sub1,sub2,sub3])
    percentage = calculate_percentage(total , 300)
    grade = calculate_grade(percentage)

    print("\n ---- Report card ----")
    print("Name:" , name)
    print("Total Marks:" , total)
    print(f"percentage: {percentage: .2f}%")
    print("Grade:", grade)

    again = input("\nwant to enter another student? (yes/no): ")
    if again.lower() != 'yes':
        break