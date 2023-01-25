# Retorna una lista de valores impares tomando en cuenta un numero limite digitado por el usuario y empezando por 1.

print("Digite el numero limite a para la lista evaluar")
length = int(input())
initial_number = 1

while initial_number <= length :
    if (initial_number % 2) != 0 :
        print(initial_number)
    initial_number += 1
else :
    print("Se alcanzo el limite de numeros")

