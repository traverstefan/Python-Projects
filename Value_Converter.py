def convert_temperature():
    print("\nWhich conversion do you want to choose:-")
    print("1. Celsius to Farenheit")
    print("2. Farenheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp} degrees Celsius is equal to {(temp * 9 / 5) + 32} degrees Farenheit.\n")
    elif choice == 2:
        temp = float(input("Enter temperature in Farenheit: "))
        print(f"{temp} degrees Farenheit is equal to {(temp - 32) * 5 / 9} degrees Celsius.\n")
    else:
        print("Invalid input...please try again!\n")

def convert_volume():
    print("\nWhich conversion do you want to choose:-")
    print("1. Fluid Ounces to Cups")
    print("2. Cups to Fluid Ounces")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        floz = float(input("Enter volume in Fluid Ounces: "))
        print(f"{floz} Fluid Ounces is equal to {(floz * 0.125)} Cups.\n")
    elif choice == 2:
        floz = float(input("Enter volume in Cups: "))
        print(f"{floz} Cups is equal to {(floz / 0.125)} Fluid Ounces.\n")
    else:
        print("Invalid input...please try again!\n")

def convert_lengths():
    print("\nWhich conversion do you want to choose:-")
    print("1. Centimeters to Feet and Inches")
    print("2. Feet and Inches to Centimeters")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter length in Centimeters: "))
        inches = value/2.54
        feet = inches/12
        print(f"{value} Centimeters is equal to {feet} Feet and {inches} Inches.\n")
    elif choice == 2:
        feet = float(input("Enter length in Feet: "))
        inches = float(input("Enter length in Inches: "))
        length = (feet * 12 + inches) * 2.54
        print(f"{feet} Feet and {inches} is {length} in Centimeters.\n")

print("===== Welcome to Value Converter =====")
while 1:
    print("Which option would you like to choose:-")
    print("1. Convert temperature")
    print("2. Convert volume")
    print("3. Convert lengths")
    print("4. I'm finished!")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_volume()
    elif choice == 3:
        convert_lengths()
    elif choice == 4:
        print('Done!')
        exit(0)
        