def km_to_mile(km):
    return km*0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius*9/5) + 32

def kg_to_pound(kg):
    return kg * 2.20462

def meter_to_cm(meter):
    return meter*100

while True:
    print("\n---- Unit Converter ----")
    print("1. Kilometer to mile")
    print("2. Celsius to fhrenheit")
    print("3. Kilogram to pound")
    print("4. Meter to centimeter")
    print("5. Exit")

    choice = input("Enter your chice (1,5) :")

    if choice == '1':
        km  = float(input("Enter Kilometers: ")) 
        miles = km_to_mile(km)
        print(f"{km} Km is {miles:.2f} miles.")
        
    elif choice == '2':
        c = float(input("Enter Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}C is {f:.2f}F.")

    elif choice == '3':
        kg = float(input("Enter Meters: "))
        pound = kg_to_pound(kg)
        print(f"{kg} Kg is {pound:.2f} pound." )

    elif choice == '4':
        m = float(input("Enter Meters: "))
        cm = meter_to_cm(m)
        print(f"{m} meter is {cm:.2f} centimeters. ")        

    elif choice == '5':
        print("Exiting... Goodbye! ")

        break

    else:
        print("Invalid choice. please enter between 1 to 5. ")


