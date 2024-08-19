# Ejercicio 1.2.1
# Análisis y Diseño de Algoritmos


# Problema 1:
    # Existe una lista de 10 nombres y se necesia encontrar el nombre `Juan`. El algoritmo es:
        # 1. Inicia la búsqueda desde la primera posición
        # 2. Mueve hacia la derecha hasta llegar a la última posición
        # 3. Compara cada nombre con `Juan`

def buscar_nombre(lista: list, nombre: str) -> int:
    """
    Busca el nombre de una persona en una lista y obtiene la complejidad del algoritmo
    por el número de pasos.
    ----
    Argumentos:
        - lista (list): Lista con los nombres de las personas
        - nombre (str): Nombre de la persona a buscar

    Salida:
        - n_pasos(int): Total de pasos que le toma al algoritmo resolver el problema
    """
    n_pasos: int = 0
    for i in range(0, len(lista)):
       n_pasos += 1
       if lista[i] == nombre:
           return n_pasos
    return -1


# Problema 2:
    # Calcular el promedio de una lista de números. El algoritmo es:
        # 1. Suma todos los números de la lista
        # 2. Divide la suma entre el total de números en la lista

def calcular_promedio(lista: list) -> tuple[int, float]:
    """
    Calcula el promedio de una serie de números y obtiene la complejidad del algoritmo
    por el número de pasos.
    Argumentos:
        - lista (list): Lista con los números

    Salida:
        - n_pasos (int): Total de pasos que le toma al algoritmo resolver el problema
    """
    n_pasos: int = 0
    suma: int = 0
    for i in range(len(lista)):
        n_pasos += 1
        suma += i
    return n_pasos, suma/len(lista)

# Problema 3:
    # Encontrar un número en una matriz de 3x3. El algoritmo es:
        # 1. Mueve hacia la derecha hasta llegar a la última columna
        # 2. Compara cada número con el número que estás buscando

def buscar_matriz(matriz:list[list], numero: int) -> int:
    n_pasos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            n_pasos += 1
            if matriz[i][j] == numero:
                return n_pasos
    return -1

if __name__ == '__main__':
    # Ejecución del Problema 1
    nombres = ["Pedro", "Juan", "Maria", "Carlos", "Juanita"]
    nombre = "Maria"
    n_pasos = buscar_nombre(nombres, nombre)
    print(f"Se necesitan {n_pasos} pasos para encontrar {nombre} en la lista {nombres}")

    # Ejecución del Problema 2
    numeros = [3, 7, 9, 11, 15]
    n_pasos, promedio = calcular_promedio(numeros)
    print(f"Se necesitan {n_pasos} para obtener {promedio} como promedio de la lista {numeros}")

    # Ejecución del Problema 3
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    numero = 7
    n_pasos = buscar_matriz(matriz, numero)
    print(f"Se necesitan {n_pasos} para encontrar el número {numero} en la matriz {matriz}")
