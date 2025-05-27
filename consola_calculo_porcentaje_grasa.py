from consola_calculo_imc import calcular_IMC
def calcular_porcentaje_grasa(peso=float, altura=float, edad=int, valor_genero=float):
    return 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero

