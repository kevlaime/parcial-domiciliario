
import os
from funciones import *
from inputs import *

array_nombres = crear_array(5,"")
matriz_puntajes = crear_matriz(5,3,0)

# array_nombres = crear_array(2,"")
# matriz_puntajes = crear_matriz(2,3,0)

bandera_carga_nombres = False
bandera_carga_votos = False

while True:
    print("1.Cargar Nombres Participantes\n2.Cargar Votos\n3.Mostrar Puntuaciones\n4.Mostrar Participantes Promedio Menor a 4\n5.Mostrar Participantes Promedio Menor a 8\n6.Mostrar Promedio de Cada Jurado\n7.Mostrar Jurado Mas Estricto\n8.Mostrar Jurado Mas Generoso\n9.Mostrar Participantes con Puntuaciones Iguales\n10.Buscar Participante Por Nombre\n11.Mostrar Participantes Ordenados Alfabéticamente\n12.Salir")

    opcion = int(input("Su opcion: "))
    while opcion > 12 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-11): "))
    if opcion == 1:
        if cargar_nombres_participantes(array_nombres) == True:
            print("Nombres cargados correctamente...")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error al realizar la carga")
    elif opcion == 2:
        if cargar_votos(matriz_puntajes) == True:
            print("Carga exitosa de votos!")
            mostrar_matriz(matriz_puntajes)
            bandera_carga_votos = True
        else:
            print("Error al realizar la carga")
    elif opcion == 3 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_votos(array_nombres, matriz_puntajes) == False:
            print("No se pueden mostrar los votos")
    elif opcion == 4 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_participantes_no_superan_puntaje_promedio(array_nombres, matriz_puntajes, 4) == False:
            print(f"No hay ningún participante con un promedio menor a 4")
    elif opcion == 5 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_participantes_no_superan_puntaje_promedio(array_nombres, matriz_puntajes, 8) == False:
            print(f"No hay ningún participante con un promedio menor a 8")
    elif opcion == 6 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_promedio_por_jurado(matriz_puntajes) == False:
             print(f"No se pueden mostrar los votos por jurado.")
    elif opcion == 7 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_jurado_mas_estricto(matriz_puntajes) == False:
             print(f"No se pueden mostrar al jurado más estricto.")
    elif opcion == 8 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_jurado_mas_generoso(matriz_puntajes) == False:
             print(f"No se pueden mostrar al jurado más generoso.")
    elif opcion == 9 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        if mostrar_participantes_puntajes_iguales(array_nombres, matriz_puntajes) == False:
             print(f"No hay ningún participante con puntuaciones iguales entre los jurados.")
    elif opcion == 10 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        nombre_buscado = input("Ingrese el nombre del participante que desea buscar: ")
        if buscar_participante_por_nombre(array_nombres, matriz_puntajes, nombre_buscado) == False:
             print(f"No hay participante con ese nombre. Vuelva a intentarlo.")
    elif opcion == 11 and (bandera_carga_votos == True and bandera_carga_nombres == True):
        ordenar_participantes_alfabeticamente(array_nombres, matriz_puntajes)
        mostrar_votos(array_nombres, matriz_puntajes)
    elif opcion == 12:
        print("Saliendo...")
        break
    else:
        print("Acceso invalido!")
    input("Toque cualquier boton para continuar...")
    os.system("clear")
