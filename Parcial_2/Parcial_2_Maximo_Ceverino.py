from is_mutant import *
# Pasos :
# - crear una lista vacia 
# -crear una función que valide que datos ingresados sean exactamente 6 y sino que devuelva un booleano 
# - crear una función que compare las letras dentro de un string y devuelva un booleano 
# - una vez estos creados formar un for pidiendo un strings y con if dentro ejecutando las funciones
# , y en caso de que todos las funciones den True se , se tendrá que separar letra por letra para crear 
# una lista y esa lista se sumara a la tabla , una vez que lala tabla tenga 6 filas se cerrara el bucle 

# ejemplo mutante [
#     "AAAAGT",
#     "TAGCTA",
#     "CATCGC",
#     "GCTAGT",
#     "TGACAC",
#     "TCTAGA" ]
#ejemplo no mutante  [
#     "ATGCAT",
#     "TAGCTA",
#     "CATCGC",
#     "GCTAGT",
#     "TGACAC",
#     "TCTAGA"


list_dna=[]
while True :
    
    if len(list_dna) == 6 :
        break
    string=input("Ingrese la primera fila para analizar").upper()
    if string.isalpha() :
        if all(character in "ACGT" for character in string):
            if  len(string) == 6 : 
                list_aux=list(string)
                list_dna.append(list_aux)
                
                
                
            else :
                print(" tienes que ingresar 6 letras por fila , pendejo")
        else :
            print("solo pueden ingresarse las letras :  A , G , C  , T ")
            
    else: 
        print("los datos son incorrectos , porfavor ingrese solo letras ")

if is_mutant(list_dna) :
    print(" Es mutante !!!!")
else:
    print("No es mutante !!!!")
