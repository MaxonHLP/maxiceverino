# 1)_Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos

import time
import os

def validator(dni):
    if len(dni)== 7 or len(dni) == 8 :
        return True
    else:
        return False

dni = input("Ingrese su DNI: ")
if dni.isnumeric():
    operator = validator(dni)
    if operator == True:
        print("Su DNI es: {}".format(dni)) 
    else:
       print("DNI incorrecto, reinicie el programa..")
else:
    print("DNI incorrecto, reinicie el programa..")    
    
time.sleep(3)    
os.system("cls")    
    

# 2)_Escribir una función que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios 
# al principio o al final del string pasado por parámetro.

def length(sentence):
    words = sentence.split()
    # Verificamos si la lista de palabras está vacía
    if not words:  
        return 0
    last_word = len(words[-1])
    return last_word

sentence = str(input("Ingrese una palabra: "))
 # Verificamos si la cadena no está vacía
if sentence.strip(): 
    print("La longitud de la última palabra de su oración es:", length(sentence))
else:
    print("Oración incorrecta, reinicie el programa.")

time.sleep(3)    
os.system("cls")


# 3)_Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso 
# de un nombre vacio.

# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será:
# nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.

# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario
# en un bucle hasta que ingrese un DNI correcto.

# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras
# del apellido y los 3 primeros dígitos de su DNI.
# Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254
import os
import time

def name_validator(completed_name):
    name1 , name2 = "" , ""
    name_parts = completed_name.split()
    
    if len(name_parts) == 1:
        name1 = name_parts[0]
    elif len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        name1, name2 = name_parts[0], name_parts[1]
    return name1, name2

def validator_dni(dni):
    if len(dni) in [7, 8] and dni.isdigit():
        return dni
    else:
        return False

def validator_dni2():
    dni_verified = ""
    while not dni_verified:
        os.system("cls")
        print("Incorrecto, intente de nuevo..")
        dni_verified = input("Ingrese correctamente el DNI: ")
        if len(dni_verified) in [7, 8] and dni_verified.isdigit():
            return dni_verified

while True:
    os.system("cls")
    completed_name = input("Ingrese su o sus nombres completos en Formato: (nombre1 nombre2): ").strip()
    dni = input("Ingrese su DNI: ")

    try:
        name1 , name2 = name_validator(completed_name)
    except ValueError:
        name1 = name_validator(completed_name)

    dni = validator_dni(dni)
    if dni is False:
        dni = validator_dni2()

    surname = input("Ingrese su apellido: ")
    if not surname.isalpha():
        print("El apellido debe contener solo letras. Intente de nuevo...")
        continue

    print(f"ID: {name1} {len(surname)} {dni[-3:]}")

    again_code = input("Desea continuar? SI/NO: ").upper()
    if again_code != "SI":
        break

time.sleep(3)
os.system("cls")

# 4)_Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

import time
import os

def is_multiple_number(number1, number2):
    if number1 % number2 == 0:
        print(f"{number1} es múltiplo de {number2}")
    elif number2 % number1 == 0:
        print(f"{number2} es múltiplo de {number1}")
    else:
        print("No son múltiplos entre sí...")

while True:
    os.system("cls")
    try:
        numbers = input("Ingrese dos números enteros separados por coma: ")
        if "," in numbers:
            number1, number2 = numbers.split(",")
            if number1.isdigit() and number2.isdigit():
                number1 = int(number1)
                number2 = int(number2)
                is_multiple_number(number1,number2)
            else:
                print("Inténtelo de nuevo..")
                continue
        else:
            print("Inténtelo nuevamente..")
            continue
    except (ValueError or TypeError):
        print("Hubo un error, inténtelo de nuevo..")
        continue

    operator = input("Desea continuar? SI/NO: ").upper()
    if operator == "NO":
        break
    else:
        continue

time.sleep(3)
os.system("cls")


# 5)_Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima 
# de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

import time, os

def mid_temp(temp_max, temp_min):
    middle_temp = (temp_max + temp_min) / 2
    return middle_temp

def average(middle_temp):
    counter = 0
    average_temp = 0

    for temp in middle_temp:
        average_temp += temp
        counter += 1

    average_temp /= counter
    return average_temp

def main():
    number_day = -1
    while number_day < 0:
        try:
            number_day = int(input("Ingrese la cantidad de días a introducir: "))
        except (ValueError, TypeError):
            print("Hubo un error, intente de nuevo..")
            time.sleep(2)
            os.system("cls")
            continue
        if number_day < 0:
            print("Incorrecto, intente de nuevo..")
            continue

    week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    middle_temp = []
    day_index = -1
    day = 0
    while day != number_day:
        day_index = (day_index + 1) % len(week)
        day += 1
        print(f"{week[day_index]} {day}: ")
        try:
            temp_max = int(input("Ingrese la temperatura máxima del día:  "))
            temp_min = int(input("Ingrese la temperatura mínima del día:  "))
            middle_temp.append(mid_temp(float(temp_max), float(temp_min)))
        except (ValueError, TypeError):
            print("Hubo un error, intente de nuevo..")
            day -= 1
            day_index -= 1
            continue

    if not middle_temp:
        print("No se introdujeron días.. Hasta luego")
    else:
        try:
            average_temp = average(middle_temp, number_day)
            print(f"Temperatura promedio total: {average_temp:.2f} ºC")
            time.sleep(3)
            os.system("cls")
        except (ValueError, ZeroDivisionError):
            print("Hubo un error, intente de nuevo..")
            time.sleep(3)
            os.system("cls")

if __name__ == "__main__":
    print("Se le solicitará a continuación la Temperatura máxima"
          " y mínima de la semana en ºC (Ingrese números enteros..)")
    main()
    

# 6)_Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras
# cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal 
# donde se use dicha función.

import time,os

def text_to_string (text):
    new_text = ""
    for letter in text:
        new_text += letter + " "
    return new_text

while True:
    try:
        text = input("Ingrese una cadena de texto: ")
        if text.isalpha():
            print(text_to_string(text))
            break
        else:
            print("Ingrese sólo texto..")
            continue
    except (TypeError):
        print("Hubo un error, intente de nuevo..")
        continue
time.sleep(3)
os.system("cls")

# 7)_Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

import os,time

def max_to_min (list_number):
    min_number = 0
    max_number = 0
    for i in list_number:
        if min_number >= i:
            min_number = i
        if max_number <= i:
            max_number = i
    new_list = [min_number,max_number]        
    return new_list

list_number = []
number = 1
print("Ingrese numeros enteros, ingrese 0 para obtener los resultados..")
while number != 0:
    try:
        number = int(input("Ingrese un numero: "))
        if number != 0:
            list_number.append(number)
        else:
            break
    except(ValueError,TypeError):
        print("Dato incorrecto, intente de nuevo..")
        continue

max_and_min_number = max_to_min(list_number)
min_number,max_number = max_and_min_number
print(f"El valor máximo ingresado es: {max_number} y el mínimo es: {min_number}")
time.sleep(3)
os.system("cls")

# 8)_Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un
# programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

import time,os,math

def area_perimeter(radio):
    area = math.pi * radio ** 2
    perimeter = math.pi * 2 * radio
    print(f"Area: {area:.2f}; Perímetro: {perimeter:.2f}")


radio = 0
while radio == 0:
    try:
        radio = float(input("Ingrese el radio de su circunferencia: "))
        if radio > 0 or radio < 0:
            area_perimeter(radio)
            break
        else:
            print("No se introdujeron valores")
            break
    except (ValueError,TypeError):
        print("Hubo un error, intente de nuevo..")
        continue

# 9)_Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero 
# si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se 
# ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
# solamente tenemos tres oportunidades para intentarlo.

import time
import os

def login(user, password, tries):
    if user == "usuario1" and password == "asdasd":
        return True, tries
    else:
        tries += 1
        return False, tries

validator_login = False
tries = 0

while tries < 3: 
    try:
        user = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")

        if user.isalnum() and password.isalpha():
            validator_login, tries = login(user, password, tries)
        else:
            tries += 1
            print(f"Incorrecto, intentos restantes {3 - tries}")
            continue

        if validator_login and tries < 3:
            print("Acceso válido")
            print("Bienvenido.")
            break
        elif tries == 3:
            print("Ha agotado los intentos.")
            time.sleep(3)
            os.system("cls")
            break

    except (ValueError, TypeError):
        tries += 1
        print(f"Incorrecto, intentos restantes {3 - tries}")

time.sleep(3)
os.system("cls")

# 10)_Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario 
# con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y 
# devolver el precio final de la compra.

import time,os

def discount_prices(prices):
    new_price = 0
    for price_values in prices.values():
       
        price_values = price_values.strip("%")
        price_values = price_values.split(",")

        price = int(price_values[0])
        discount = int(price_values[1])
        
        price_with_discount = price - (price * (discount / 100))
        new_price += price_with_discount

    return new_price

if __name__ == "__main__":
    prices = {1: "1000,20%", 2: "1500,30%", 3: "2000,10%", 4: "3000,20%", 5: "5000,20%"}
    new_price = discount_prices(prices)
    print(f"El precio total con los descuentos de cada producto es: {new_price}")
time.sleep(3)
os.system("cls")    


# 11)_Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar
# la función dada a cada uno de los elementos de la lista.

import time,os

def multiplication (list1):
    new_list = []
    for number in list1:
        new_list.append(number * 2)
    return new_list

def exponent_list (list1):
    new_list = multiplication(list1)
    final_list = []
    for number in new_list:
        final_list.append(number ** 2)
    return final_list    

if __name__ == "__main__":
    list1 = [2,4,6,8,10]
    final_list = exponent_list(list1)
    print("Se introduce una lista con valores iniciales, se los multiplica por 2 y luego se lo eleva al cuadrado..")
    print(f"Lista Inicial: {list1}")
    print(f"Lista final: {final_list}")

time.sleep(5)
os.system("cls")

# 12)_Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su 
# longitud.

import time,os

def string_to_dict (string):

    string = string.strip()
    string = string.split(" ")
    
    # string_dict = {word: len(word) for word in string} 

    string_dict = {}
    for word in string:
        string_dict [word] = len(word)

    return string_dict 


if __name__ == "__main__":
    string = input("Ingrese una frase: ")
    string_dict = string_to_dict(string)
    print(f"La frase convertida a diccionario es: {string_dict}")

time.sleep(5)
os.system("cls")

# 13)_Escribir una función que calcule el módulo de un vector.
import time,os
def module_vect (mass,aceleration):
    force = mass *aceleration
    return force

while True:
    try:
        mass = float(input("Ingrese la masa: "))
        aceleration = float(input("Ingrese el valor de la aceleración: "))
        force = module_vect(mass,aceleration)
        print(f"Vector Fuerza: {force} N")
        break
    except (ValueError,TypeError):
        print("Hubo un error, intente de nuevo..")
        continue

time.sleep(3)
os.system("cls")


# 14)_Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función
# booleana que lo decida.

import time,os

def prime_validator (prime_number):
    if (prime_number % 2 != 0) and (prime_number % 3 != 0) and (prime_number % 5 != 0) and (prime_number % 7 != 0):
        return True
    else:
        return False

while True:
    try:
        prime_number = int(input("Ingrese un número entero: "))
        operator = prime_validator(prime_number)
        if operator == True:
            print(f"{prime_number} es un número primo.")
        else:
             print(f"{prime_number} no es un número primo.")
        break
    except(ValueError,TypeError):
        print("Ingreso un comando incorrecto, intente de nuevo..")
        continue
time.sleep(3)
os.system("cls")

# 15)_Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la 
# cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

import time,os

def factorial_number(number):
    factorial = 0
    if number == 0:
        return 1
    else:
        while number != 0:
            factorial += number
            number -= 1
        return factorial

def main_factorial(number):
    if number >= 0:
            factorial = factorial_number(number)
            print(f"El Factorial del número {number} es: {factorial}")
    else:
        print("Por favor ingrese un número positivo o nulo..")
        return False 
    operator = input("Desea continuar? SI/NO: ").upper()
    if operator == "NO":
        print("Hasta luego.")
        time.sleep(3)
        os.system("cls")
        return True
    else:
        return False

while True:
    try:
        number = int(input("Ingrese un número entero: "))
        operator = main_factorial(number)
        if operator == False:
            continue
        else:
            break
    except(ValueError,TypeError):
        print("Ingreso un comando incorrecto, intente de nuevo..")
        continue

# 16)_Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito 
# en el número, utilizando para ello una función que calcule la frecuencia.

import time,os

def number_digit (number,digit):
    number = str(number)
    digit = str(digit)
    counter = 0
    for digit_in_number in number:
        if digit == digit_in_number:
            counter += 1
    return counter

def validator_number_digit(number,digit):
    if number >= 0 and (digit >= 0 and digit <= 9):
        return True
    else:
        return False

while True:
    try:
        number = int(input("Ingrese un número entero: "))
        digit = int(input("Ahora ingrese un dígito (0-9): "))
        operator = validator_number_digit(number,digit)
        if operator == True:
            counter = number_digit(number,digit)
            print(f"El dígito {digit} se repite {counter} veces en el número {number}. ")
            time.sleep(3)
            os.system("cls")
            break
        else:
            print("Uno de los valores ingresados es incorrecto, intentelo nuevamente: ")
            continue
    except(ValueError,TypeError):
        print("Dato incorrecto, intente de nuevo: ")
        continue


# 17.Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no
# sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar
# la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial 
# del mayor número ingresado.

import time,os

def bigger_prime_number(prime_number):
    bigger_number = 0
    if prime_number > bigger_number:
        bigger_number = prime_number
    return bigger_number    

def number_digit (prime_number,digit):
    prime_number = str(prime_number)
    digit = str(digit)
    sum_digit = 0
    counter = 0
    for digit_in_number in prime_number:
        sum_digit += int(digit_in_number)
        if digit == digit_in_number:
            counter += 1
    return counter,sum_digit

def validator_number_digit(number,digit):
    if number >= 0 and (digit >= 0 and digit <= 9):
        return True
    else:
        return False

while True:
    try:
        digit = int(input("Ingrese un dígito (0-9): "))
        prime_number = int(input("Ingrese un número primo, ingrese un numero no primo para salir: "))
       
        operator = validator_number_digit(prime_number,digit)
        if operator == True:
            if prime_number % 2 != 0 and  prime_number % 3 != 0 and  prime_number % 5 != 0 and  prime_number % 7 != 0:
                counter,sum_digit = number_digit(prime_number,digit)
                bigger_number = bigger_prime_number(prime_number)
                print(f"El dígito {digit} se repite {counter} veces en el número {prime_number}. ")
                print(f"La suma de los dígitos del numero primo es: {sum_digit}")
            else:
                break
    except(ValueError,TypeError):
        print("Dato incorrecto, intente de nuevo: ")
        continue

print(f"El mayor numero primo ingresado fue: {bigger_number}.")
time.sleep(3)
os.system("cls")