# Crear una aplicacion para calcular el IMC (INDICE DE MASA CORPORAL)
# IMC = peso / (altura)^2

print("APLICACION CALCULADORA DE INDICE DE MASA CORPORAL")

print("Digite su peso:")
peso = float(input())

print("Digite su altura:")
altura = float(input())

imc = round((peso / altura**2), 2)


print("Su Indice de masa corporal es:", imc)
