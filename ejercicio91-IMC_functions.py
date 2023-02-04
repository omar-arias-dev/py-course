# Crear una aplicacion para calcular el IMC (INDICE DE MASA CORPORAL)
# IMC = peso / (altura)^2
# IMC < 18.5 -> Peso bajo
# IMC >= 18.5 & <= 29.9 -> Peso normal
# IMC > 29.9 -> Obesidad

def start_app() :

    peso = 0
    altura = 0

    while peso < 30 :
        print("Escribe tu peso (En kigramos)")
        peso = float(input())
        if peso < 30 :
            print("Escribe un peso correcto")

    while altura < 1.30 :
        print("Escribe tu altura (en metros)")
        altura = float(input())
        if altura < 1.30 :
            print("Escribe una altura correcta")

    imc = calculate_imc(peso, altura)
    status = define_status(imc)
    print("Tu índice de masa corporal es", imc)
    print("Tu estado actual es", status)



def calculate_imc(peso, altura) :
    return round(peso / altura**2)



def define_status(imc) :
    if imc < 18.5 :
        return "Peso bajo"
    elif imc >= 18.5 and imc <= 29.9 :
        return "Peso normal"
    else :
        return "Obesidad"


start_app()