from msilib import sequence


def is_mutant(dni):
    letter_equal=0
    sequence_counter=0
    
    # Recorriendo las filas del DNI (6 filas)
    for row in range(6):
        letter_equal=0
        
        # Recorriendo las columnas (5 columnas)
        for column in range(5):
            # Comparando la letra actual con la siguiente en la misma fila
            if dni[row][column] == dni[row][column+1]:
                letter_equal += 1  # Incrementa el contador de letras iguales
            else:
                letter_equal = 0  # Reinicia el contador si no son iguales
        letter_equal=0
        # Verificando si hay una secuencia de al menos 4 letras iguales en la misma fila
        if letter_equal >= 4:
            sequence_counter += 1  # Incrementa el contador de secuencias
            letter_equal = 0  # Reinicia el contador de letras iguales para la siguiente fila

    
    # Bucle externo: Itera a través de las columnas (índice de columna de 0 a 5)
    for column in range(6):
        # Bucle interno: Itera a través de las filas (índice de fila de 0 a 4)
        letter_equal=0
        for row in range(5):
            # Compara el elemento en la fila actual con el elemento en la fila siguiente
            
            if dni[row][column] == dni[row+1][column]:
                letter_equal += 1  # Si son iguales, incrementa el contador
                
            else:
                letter_equal = 0  # Si no son iguales, reinicia el contador
            letter_equal=0
        # Verifica si hay una secuencia de al menos 4 elementos iguales en la columna actual
        if letter_equal >= 4:
            
            sequence_counter += 1  # Incrementa el contador de secuencias
            letter_equal = 0  # Reinicia el contador de letras iguales
            
    letter_equal = 0  # Reinicia el contador de letras iguales para su uso posterior
    
    #empezamos las comparaciones de las secuencias diagonal    
    for row in range(5):
        for column in range(5):
            # Inicializando el contador de letras iguales
            letter_equal = 0

           # Recorriendo una secuencia de 5 letras en diagonal
            for letter in range(5):
                # Compara la letra actual con la siguiente en la diagonal
                if dni[row][column] == dni[row + 1][column + 1]:
                    letter_equal += 1
                else:
                    letter_equal = 0

            # Si encontramos una secuencia de 4 letras iguales en diagonal, incrementamos el contador de secuencias
            if letter_equal >= 4:
                sequence_counter += 1
                letter_equal = 0


    # Comprobando si hay al menos dos secuencias de 4 letras iguales en diagonal
    if sequence_counter >= 2:
        print(sequence_counter)
        return True 
    else :
        print(sequence_counter)
        return False
        

