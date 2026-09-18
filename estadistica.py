# Programa que calcula estadisticas basicas de una lista de numeros: cantidad, suma, promedio, minimo y maximo

def calcular_estadisticas(numeros):
    cantidad = len(numeros)
    suma_total = sum(numeros)
    promedio = suma_total / cantidad
    minimo = min(numeros)
    maximo = max(numeros)
    return cantidad, suma_total, promedio, minimo, maximo


def leer_numeros():
    entrada = input("Ingrese una lista de numeros separados por comas: ")
    if entrada.strip() == "":
        raise ValueError("Error: no puedes ingresar vacio.")

    numeros = []
    for texto in entrada.split(","):
        texto = texto.strip()
        if texto == "":
            continue
        numeros.append(float(texto))

    if len(numeros) == 0:
        raise ValueError("Error: debes ingresar al menos un numero.")

    return numeros


def main():
    print("=== CALCULADORA DE ESTADISTICAS BASICAS ===")

    try:
        numeros = leer_numeros()
    except ValueError as e:
        print(str(e))
        return

    cantidad, suma_total, promedio, minimo, maximo = calcular_estadisticas(numeros)

    print("\n--- Resultados ---")
    print(f"Cantidad: {cantidad}")
    print(f"Suma: {suma_total}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Minimo: {minimo}")
    print(f"Maximo: {maximo}")


if __name__ == "__main__":
    main()