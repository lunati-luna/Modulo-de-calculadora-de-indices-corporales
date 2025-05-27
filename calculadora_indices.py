from consola_calculo_imc import calcular_IMC, clasificar_IMC
from consola_calculo_porcentaje_grasa import calcular_porcentaje_grasa
from consola_calculo_calorias_reposo import calcular_calorias_en_reposo
from consola_calculo_calorias_actividad import calcular_calorias_en_actividad
from consola_calculo_calorias_adelgazar import consumo_calorias_recomendado_para_adelgazar

def pedir_float(mensaje):
    while True:
        entrada = input(mensaje).replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Por favor, ingrese un número válido (use ',' o '.' para los decimales).")

def pedir_int(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def continuar():
    while True:
        respuesta = input("¿Desea realizar otro cálculo? (Si/No): ").strip().lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            print("Módulo cerrado")
            return False
        else:
            print("Por favor, responda 'Si' o 'No'.")


def mostrar_menu():
    print("\nCalculadora de Índices Corporales")
    print("1. Calcular IMC")
    print("2. Calcular Porcentaje de Grasa Corporal")
    print("3. Calcular Calorías en Reposo (TMB)")
    print("4. Calcular Calorías según Actividad Física")
    print("5. Calorías para Adelgazar")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            peso = pedir_float("Ingrese su peso en kg: ")
            altura = pedir_float("Ingrese su altura en metros: ")
            imc = calcular_IMC(peso, altura)
            print(f"Su IMC es: {imc:.2f}")
            clasificacion = clasificar_IMC(imc)
            print(f"Clasificación: {clasificacion}")
            if not continuar():
                break
        
        elif opcion == "2":
            peso = pedir_float("Ingrese su peso en kg: ")
            altura = pedir_float("Ingrese su altura en metros: ")
            edad = pedir_int("Ingrese su edad: ")
            valor_genero = pedir_float("Ingrese 0 si es mujer, 10.8 si es hombre: ")
            grasa = calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
            print(f"Su porcentaje de grasa corporal estimado es: {grasa:.2f}%")
            if not continuar():
                break
            

        elif opcion == "3":
            peso = pedir_float("Ingrese su peso en kg: ")
            altura = pedir_float("Ingrese su altura en cm: ")
            edad = pedir_int("Ingrese su edad: ")
            valor_genero = pedir_int("Ingrese 5 si es hombre, -161 si es mujer: ")
            tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
            print(f"Su Tasa Metabólica Basal (TMB) es: {tmb:.2f} calorías/día")
            if not continuar():
                break

        elif opcion == "4":
            peso = pedir_float("Ingrese su peso en kg: ")
            altura = pedir_float("Ingrese su altura en cm: ")
            edad = pedir_int("Ingrese su edad: ")
            valor_genero = pedir_int("Ingrese 5 si es hombre, -161 si es mujer: ")
            valor_actividad = pedir_float("Ingrese el factor de actividad (ej: 1.2 sedentario, 1.55 moderado, etc.): ")
            calorias_actividad = calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
            print(f"Su requerimiento calórico diario según actividad es: {calorias_actividad:.2f} calorías/día")
            if not continuar():
                break

        elif opcion == "5":
            peso = pedir_float("Ingrese su peso en kg: ")
            altura = pedir_float("Ingrese su altura en cm: ")
            edad = pedir_int("Ingrese su edad: ")
            valor_genero = pedir_int("Ingrese 5 si es hombre, -161 si es mujer: ")
            mensaje = consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
            print(mensaje)
            if not continuar():
                break

        elif opcion == "0":
            print("Módulo cerrado")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()


