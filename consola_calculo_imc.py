def calcular_IMC(peso=float, altura=float):
    return peso / (altura ** 2) 
    
def clasificar_IMC(imc):
    if imc < 16:
        return "Delgadez severa"
    elif imc < 17:
        return "Delgadez moderada"
    elif imc < 18.5:
        return "Delgadez aceptable"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    elif imc < 50:
        return "Obesidad tipo III o mórbida"
    else:
        return "Obesidad tipo IV o extrema"
