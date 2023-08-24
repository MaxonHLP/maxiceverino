

""""Un instituto de inglés necesita un programa que le permita, cada día, procesar
observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
distintos niveles y cada nivel tiene clases en un día de la semana diferente: *los lunes se
dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los
jueves son para práctica hablada y los viernes se dicta inglés para viajeros*

Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.

Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $"""

#Se solicita la fecha actual en el formato adecuado
fecha=input(" ingrese la fecha actual ; el dia , mes  y dia de la semana en formato [DIA , DD/MM ]")

#Se definen las variables y asigna el valor corespondiente
dia_semana= fecha[0:fecha.find(',')]
dia_semana=dia_semana.lower()
dia =int(fecha[fecha.find(' ')+1:fecha.find('/')])
mes=int(fecha[fecha.find('/')+1:len(fecha)])







#Se determina que fecha ingreso el usuario para asi poder dirigirlo a las distintas actividades que han tenido los alumnos
if dia_semana=="lunes" or dia_semana=="martes" or dia_semana=="miércoles" or dia_semana=="jueves" or dia_semana=="viernes" :
    print("")
    if dia>1 or dia<31:
        print("")
        if mes>=7 and mes<=12:
            print("Fecha ingresada: " ,dia_semana,dia,"/",mes )
            if dia_semana=="lunes":
               #El dia lunes se tomo examen al nivel inicial, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
               print("______________ Hoy se tomaron examenes al nivel inicial ______________")
               examenes_aprobados=int(input("_ Ingrese el número de alumnos aprobados: "))
               examenes_desaprobados=int(input("_ Ingrese el número de alumnos desaprobados:"))
               porcentaje_aprobados=(examenes_aprobados*100)/30
               print("- Aprobaron el ", porcentaje_aprobados, " porciento de los alumnos en nivel inicial -")
               porcentaje_desaprobados=(examenes_desaprobados*100)/30
               print("- Y desaprobaron el ", porcentaje_desaprobados, " porciento de los alumnos en nivel inicial -")
            else:
                #El dia martes se tomo examen al nivel intermedio, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
                if dia_semana=="martes":
                  print("______________ Hoy se tomaron examenes al nivel intermedio ______________")
                  examenes_aprobados=int(input("_ Ingrese el número de alumnos aprobados: "))
                  examenes_desaprobados=int(input("_ Ingrese el número de alumnos desaprobados: "))
                  porcentaje_aprobados=(examenes_aprobados*100)/60
                  print("- Aprobaron el ", porcentaje_aprobados, " porciento de los alumnos en nivel intermedio -")
                  porcentaje_desaprobados=(examenes_desaprobados*100)/60
                  print("- Y desaprobaron el ", porcentaje_desaprobados, " porciento de los alumnos en nivel intermedio -")
                else:
                    #El dia miercoles se tomo examen al nivel avanzado, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
                    if dia_semana=="miércoles":
                       print("______________ Hoy se tomaron examenes al nivel avanzado ______________")
                       examenes_aprobados=int(input("_ Ingrese el numero de alumnos aprobados: "))
                       examenes_desaprobados=int(input("_ Ingrese el numero de alumnos desaprobados: "))
                       porcentaje_aprobados=(examenes_aprobados*100)/60
                       print("- Aprobaron el ", porcentaje_aprobados, " porciento de los alumnos en nivel avanzado -")
                       porcentaje_desaprobados=(examenes_desaprobados*100)/60
                       print("- Y desaprobaron el ", porcentaje_desaprobados, " porciento de los alumnos en nivel avanzado -")
                    else:
                        #El dia jueves hubo practica hablada, el usuario puede ver la cantidad de alumnos que asistieron y los que no
                        if dia_semana=="jueves":
                            print("______________ Hoy no se tomaron examenes hubo Practica Hablada ______________")
                            alumnos_presentes=int(input("_ Ingrese el porcentaje de alumnos que asisterieron a clases: "))
                            if alumnos_presentes>=50:
                                print("- Asistio la mayoria de los alumnos -")
                            else:
                                print("- No asistio la mayoria de los alumnos -")
                        #El dia viernes hubo ingles para viajeros, el usuario puede igresar la cantidad de alumnos que ingresaron al nuevo ciclo y puede ver el ingreso total de la institucion
                        if dia_semana=="viernes":
                            print("______________ Hoy no se tomaron examenes hubo Ingles para Viajeros ______________")
                            if dia==1 and mes==1 or mes==7:
                                print("Comienzo de nuevo ciclo")
                                cantidad_alumnos=int(input("_ Ingrese la cantidad de alumnos que ingresan al nuevo ciclo: "))
                                arancel_alumno=int(input("_ Ingrese el arancel en ($) por cada alumno: "))
                                total_ingreso=cantidad_alumnos*arancel_alumno
                                print("_ El ingreso total es de: $",total_ingreso)
        else:
            print("Fecha incorrecta")
    else:
        print("Fecha incorrecta")
else:
 print("Fecha incorrecta")


