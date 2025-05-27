from consola_calculo_calorias_reposo import calcular_calorias_en_reposo
def consumo_calorias_recomendado_para_adelgazar(peso=float, altura=float, edad=int, valor_genero=int):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    minimo = tmb * 0.80
    maximo = tmb * 0.85
    return f"Para adelgazar, debe consumir entre {minimo:.2f} y {maximo:.2f} calorías al día."