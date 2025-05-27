from consola_calculo_calorias_reposo import calcular_calorias_en_reposo
def consumo_calorias_recomendado_para_adelgazar(peso=float, altura=float, edad=int, valor_genero=int):
    return calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.85