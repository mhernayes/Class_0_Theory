#In this document will see how to work whit "Loops".

fruits = ["apple", "orange", "pears", "cherries", "grapes"]

# for
for i in fruits:
    print("Would yo like {} ?".format(i))

for i in range(1,11):
    print("Number {}".format(i))

# defino variable y seteo en 37
temp = 37

# while
while temp > 32:
    print("The water temperature is {}".format(temp))
    temp -= 1

# loop controls
# "Break" ends the loop
# "Continue" skips current part of the loop/moves to the next part of the loop (va a la siguiente iteracion)
# "Pass" skips any parts of the loop where "pass" appears.

temp == 38
while temp > 32:
    print("The water temperature is {}".format(temp))
    temp -= 1
    if temp == 35:
        break

for number in range(1,11):
    if number == 7:
        print("We are skipping number 7.")
        continue
    print("This is the number {}".format(number))

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}".format(number))

import time

temporizador = int(input("introduce el numero de segundos "))

print("comienza el temporizador")

for i in range(0, temporizador, 1): #el ultimo 1 es cada cuanto avanza el for
    print("Quedan ", temporizador, " segundos")
    time.sleep(1)
    temporizador = temporizador - 1

print("El temporizador ha finalizado")
