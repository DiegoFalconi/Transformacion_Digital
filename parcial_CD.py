def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        numeros (list): Lista de valores numéricos.

    Retorna:
        float: Promedio de los números de la lista.
    """
    return sum(numeros) / len(numeros)


# Ejemplo de uso
datos = [19, 10, 77, 51, 13]
print(calcular_promedio(datos))