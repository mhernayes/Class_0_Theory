#In this document will see how to work whit "Variables".

#definir variables

_cars = 23
cars = 24
CARS = 25
number_of_cars = 23

print(cars)
print(_cars)
print(CARS)

"""
This is an example
"""

name = 'HOLA'
type_of_car = "super auto"


print(name + " " + type_of_car)

print("{}, {}".format(name, type_of_car))

def addition():
    a = float(input("enter a number. "))
    b = float(input("enter the second number. "))
    #formate los floats con 2 decimales
    print("El resultado total es {:.2f} {:.2f}".format(a,b))
    c = a + b
    print("El resultado total es {:.2f}".format(c))
addition()
''' this is an example'''

""" 
this is an example

"""

def user(name, age=0, city="Tucson"):
    print("{} is {} years old and lives in {}".format(name, age, city))

user("Carlos", 56, "Oklahoma")
user("tomas")

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

application("Jess", "Ingrass", "mail@mail.com", "TechCode.org", 75000, hire_date = "September 2010")

x, y, z = 10, 20, 30

print(x, y, z)