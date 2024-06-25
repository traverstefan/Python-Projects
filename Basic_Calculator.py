def addition ():

    print("Addition")

    n = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    return n + b

def subtraction ():

    print("Subtraction")

    n = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    return n - b

def multiplication ():

    print("Multiplication")

    n = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    return n * b

def division ():

    print("Division")

    n = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    return n / b

#Main

while True:

    res = []

    print(" My Calculator")

    print(" Enter 'a' for addition")

    print(" Enter 's' for subtraction")

    print(" Enter 'm' for multiplication")

    print(" Enter 'd' for division")

    print(" Enter 'q' to quit")

    c = input(" ")
    if c != 'q':
        if c == 'a':
            res = addition()
            print("Answer = ", res)
        elif c == 's':
            res = subtraction()
            print("Answer = ", res)
        elif c == 'm':
            res = multiplication()
            print("Answer = ", res)
        elif c == 'd':
            res = division()
            print("Answer = ", res)
    else:
        print("Exiting...")
        break
