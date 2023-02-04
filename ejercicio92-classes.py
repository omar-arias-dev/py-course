class CalcularIMC :

    def __init__(self, peso, altura) : # Constructor
        self.peso = peso
        self.altura = altura
        self.imc = 0
    
    def get_imc(self) : # Funcion o metodo de clase
        self.imc = round(self.peso / self.altura**2)
        return self.imc



class MostrarPesoIdeal(CalcularIMC) : # Herencia

    def imprimir_peso(self):
        print(self.imc)



obj = MostrarPesoIdeal(86, 1.74) # Se crea instancia
obj.get_imc()
obj.imprimir_peso()
