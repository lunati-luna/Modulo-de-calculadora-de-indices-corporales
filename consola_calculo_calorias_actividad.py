
from consola_calculo_calorias_reposo import calcular_calorias_en_reposo 
def calcular_calorias_en_actividad(peso=float, altura=float, edad=int, valor_genero=int, valor_actividad=float):
    return calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad





