#In this document will see how to work whit a "Calculator".

print(1 < 1)
print(1 == 1)
print(1 > 1)

name = input("What is your name? ")
if name == "Jess":
    print("Hi, {}".format(name))
elif name == "Daniel":
    print("Hello, you are a great person, {}".format(name))
print("have a nice day")

on = True

def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print (a + b)

def substraccion():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print (a - b)

def multiplication():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print (a * b)

def division():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print (a / b)

while on:
    operation = input("Please type +, -, *, /, or q ")
    if operation == "+":
        add()
    elif operation == "-":
        substraccion()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    elif operation == "q":
        on = False
    else:
        print("That operation is not valid")