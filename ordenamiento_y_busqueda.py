# TIPOS DE ORDENAMIENTO:

# Ordenamiento de Burbuja (Bubble Sort):

arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr) - 1):
    for j in range(0, len(arr)-1- i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Arreglo ordenado con Bubble Sort:", arr)

# Ordenamiento por Selección (Selection Sort):

arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Arreglo ordenado con Selection Sort:", arr)

# Ordenamiento por Inserción (Insertion Sort):

arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Arreglo ordenado con Insertion Sort:", arr)

# Ordenamienro por Combinacion (Merge Sort)

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Arreglo ordenado:", arr)


# TIPOS DE BUSQUEDA:

# Busqueda Lineal:

'Lista en la que vamos a buscar el elemento'
lista = [5, 12, 34, 7, 2, 19, 45, 8]

'Elemento que queremos buscar'
elemento_buscado = 7

'Variable para almacenar el índice donde se encontró el elemento (si se encuentra)'
indice = -1

'Recorremos la lista de manera lineal para buscar el elemento'
for i in range(len(lista)):
    if lista[i] == elemento_buscado:
        indice = i
        'Terminamos la búsqueda una vez que encontramos el elemento'
        break  

'Comprobamos si se encontró el elemento'
if indice != -1:
    print(f"Elemento {elemento_buscado} encontrado en el índice {indice}.")
else:
    print(f"Elemento {elemento_buscado} no encontrado en la lista.")

# Busqueda Binaria:

'Lista ordenada en la que vamos a buscar el elemento'
lista = [2, 5, 7, 12, 19, 34, 45, 67, 89]

'Elemento que queremos buscar'
elemento_buscado = 19

'Inicializamos los punteros izquierda y derecha'
izquierda, derecha = 0, len(lista) - 1

'Bucle para realizar la búsqueda binaria'
while izquierda <= derecha:
    medio = (izquierda + derecha) // 2

    if lista[medio] == elemento_buscado:
        print(f"Elemento {elemento_buscado} encontrado en el índice {medio}.")
        'Hemos encontrado el elemento, podemos salir del bucle'
        break 
    elif lista[medio] < elemento_buscado:
        izquierda = medio + 1
    else:
        derecha = medio - 1
else:
    print(f"Elemento {elemento_buscado} no encontrado en la lista.")