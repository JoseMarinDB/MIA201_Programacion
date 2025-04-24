
import random

def suma(a, b):
    print(a + b)
    res = a + b
    return res


def resta(a, b):
    res =  b - a
    return res

def generar_lista_al_azar(n, semilla=None):
    """
    Función que genera una lista de n números enteros aleatorios entre 1 y 100.
    param n: número de elementos de la lista
    param semilla: semilla para la generación aleatoria
    return: lista de números aleatorios
    """
    if semilla is not None:
        random.seed(semilla)

    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

def primer_minimo_menor_que(b, l):
    """
    Función que devuelve el primer mínimo menor a b de una lista l.
    """
    i = 0
    while l[i] > b and i<(len(l)-1):
        i = i + 1

    return l[i]


def factorial(n):
    if n == 0:
        res = 1
    else:
        res = n * factorial(n - 1)
    return res


if __name__ == "__main__":
    # Corriendo el código
    print("Corriendo el código")
else:
    print("Código importado como módulo")
