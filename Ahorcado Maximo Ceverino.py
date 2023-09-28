import random
#Define una lista de palabras que el programa pueda elegir al azar para que el jugador
#adivine. Puedes usar palabras relacionadas con la programación, tecnología o
#cualquier tema que te guste.
# El programa debe seleccionar una palabra al azar de la lista para cada partida.
# El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
#representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
#lugar correspondiente.
# El jugador debe poder ingresar una letra adivinada en cada turno.
# El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el
#tablero en consecuencia.
# El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el
#juego.
# Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente"
#o "Letra incorrecta, te quedan X intentos".
# El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin
#intentos.
# Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de
#derrota si se quedan sin intentos.

words=["azul" , "violeta" , "naranja" , "fucsia" , "amarillo" , "gris", "indigo" , "rojo" , "verde" , "marron"]
#lista de palabras a adivinar

def select_word():
    return random.choice(words)
#funcion para seleccionar una palabra aleatoria 

#formacion de funcion inicializadora
def initialize(word):
    return['_' for _ in word]
#itera a través de cada letra de la palabra que se pasa como argumento, creando un número igual de guiones bajos como letras en la palabra.

#funcion para mostrar el tablero 
def show_board(board):
    return" ".join(board) #join() se utiliza para combinar los elementos de una secuencia (como una lista, tupla o conjunto) en una sola cadena de texto. 
#Estamos uniendo los elementos del tablero con un espacio en blanco " ", para que el contenido del tablero sea mas facil de leer.

# Función principal del juego.
def hanged():
    secret_word = select_word()
    attempts_remaining = 6
    guessed_letters = []
    board = initialize(secret_word)
    
    print("¡Bienvenido al Juego del Ahorcado!")
    print("Tienes que adivinar un color .")
    
    while True:
        # Muestra el estado actual del tablero del juego.
        print("\n" + show_board(board))
        # Solicita al jugador ingresar una letra y la convierte a minúsculas.
        letter = input("\nIngresa una letra: ").lower()
        
        # Verifica que la entrada sea una letra y que la longitud de la cadena letra sea exactamente 1.
        if not letter.isalpha() or len(letter) != 1:
            print("¡Caracter erroneo!, ingrese una sola letra.")
            continue

        # Verifica si la letra ya ha sido adivinada previamente.
        if letter in guessed_letters:
            print("Ya adivinaste esa letra.")
            continue
        
        # Verifica si la letra ingresada está en la palabra secreta.
        if letter in secret_word:

            guessed_letters.append(letter) # Agrega la letra a la lista de letras adivinadas.

            # Actualiza el tablero con la letra adivinada en las posiciones correctas.
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    board[i] = letter
            print("Adivinaste una letra correctamente.")

        else:
            attempts_remaining -= 1 #Reduce el número de intentos restantes en caso de una adivinanza incorrecta.
            print(f"Letra incorrecta, te quedan {attempts_remaining} intentos.")
        
        # Verifica si ya se adivinaron todas las letras en el tablero.
        if "_" not in board:
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            print(f"La palabra era: {secret_word}")
            break

        # Verifica los intentos restantes.
        if attempts_remaining == 0:
            print("\n¡Has agotado tus intentos! Perdiste.")
            print(f"La palabra era: {secret_word}")
            break

# Iniciar el juego.
hanged()