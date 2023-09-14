# 1)_Create a while loop with the following characteristics:

# The initial value of the variable x will be 0.
# The increment value will be 1.
# The exit condition of the loop will be greater than or equal to 30.
# The execution must be broken when x is equal to 15.
# You must print the following sentence each time the loop executes:
# 'The value of the loop is: ' + x.
# You must skip the executions with the value of x in 4, 6 and 10.
# At each execution jump, you must display the jumped values with this message:
# 'The value ' + x ' of x was skipped'.
# When the execution of the loop is broken, you must show a message indicating it: 
# 'The execution of the loop was broken when x was ' + x.

x=0
while x <= 30:
    x += 1
    if x == 15: 
        break
    elif x == 4 or x == 6 or x == 10:
        print("The value",x," of x was skipped.")
        continue
    else:
        print(x)
print("The execution of the loop was broken when x was ",x)

# 1)_ Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas 
# en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
sequence=""
print("Deje un espacio en blanco para salir")
while True:
    line = str(input("Ingrese su linea: ")).upper()
    if line:
        sequence += line + " "
    else:
        break
print(sequence)    

# 2)_Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50
# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos
# Ejemplo de una entrada:
# D 200
# D 200
# R 100
# D 50
# Introducir una línea vacía indica que ha finalizado la bitácora.
# La salida de éste programa sería:
# 350
total=0
print("Deje un espacio en blanco para salir")
while True:
    print("Saldo Disponible: $",total)
    print("Ingrese su operacion (D:deposito / R:retiro): ")
    operator=str(input()).upper()
    if operator:
        if operator == "R" or operator== "D":
            amount=int(input("Ingrese su monto: "))
            if amount >= 0:
                if operator == "R":
                    if total >= amount:
                        total -= amount
                        print("Usted retiro: $",amount)
                        print("-----------------------------")
                    else:
                        print("Fondos insuficientes.")
                if  operator == "D":
                    total += amount
                    print("Usted deposito: $",amount)
                    print("-----------------------------")
    else:
        break                
print("Resumen final: Usted posee $",total,". Gracias por su visita.")                    

# 3)_Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores
# que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos:
# él mismo y el 1.
number=1
prime_number=0
list=[]
while number !=0:
    print("Ingrese numeros mayores a 1 (ingrese 0 para salir)")
    number=int(input("Ingrese un número: "))
    if number > 1:
        if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            prime_number += 1 
            list.append(number)
    elif number == 0:
        break        
print("La cantidad total de números primos ingresados fue: ",prime_number)
print("Los numeros primos fueron: ",list)

# 4)_Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años
# en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
# excepto que también sea divisible por 400.
year1=int(input("Ingrese el 1º año: "))
year2=int(input("Ingrese el 2º año: "))
list=[]
if year1 <= year2:
    for i in range(year1,year2):
        if i % 10 == 0:
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                list.append(i)
    print("Los años bisiestos y múltiplos de 10 son: ",list)            
else: 
    print("El 1º año debe ser mayor o igual al segundo")

# 5)_Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for.
# Utiliza la declaración continue para omitir los númxeros impares.
print("Numeros pares del 1 al 20.")
for i in range(1,21,1):
    if i % 2 != 0:
        continue
    else:
        print(i)

# 6)_Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
# Cuando encuentres el número, usa break para salir del bucle.
list=[1,2,3,4,5,6,7,8,9,10]
target_number = 7
for position, i in enumerate(list):
    if target_number == i:
        print("Su numero ",target_number," se encuentra en la lista en la posición", position)
        break

# 7)_Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
# Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0",
# utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
import os
import time
number=1
total=0
while number != 0:
    os.system("cls")
    print("Menú de Opciones: ")
    print("0: Salir.")
    print("1: Preguntar saldo.")
    print("2: Depositar fondos.")
    print("3: Retirar fondos.")
    print("---------------------------")
    number=int(input("Ingrese su operacion: "))
    if number == 0:
        break
    elif number == 1:
        print("Saldo Actual: $",total)
    elif number == 2:
        amount=int(input("Ingrese su monto: $ "))
        total += amount
        print("Usted depositó: $",amount)
    elif number == 3:
        amount=int(input("Ingrese su monto: $ "))
        if total >= amount:
            total -= amount
            print("Usted retiró: $",amount)
        else:
            print("Fondos insuficientes.")
    else:    
        print("Comando incorrecto.")
        continue    
    
    print("Aguarde 3 segundos...")
    time.sleep(3)
print("Gracias por su visita.")