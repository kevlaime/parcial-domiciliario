from funciones import *

def cargar_nombres_participantes(array_nombres:list) -> bool:
    """Se encarga de cargar el nombre de los participantes.
    Args:
        array_nombres (list): La lista original donde va hacer la modificacion.
    Returns:
        bool: True si recibe como parametro una lista con valores. Sino False.
    """
    if type(array_nombres) == list and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            while True:
                nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
                if es_alfabetico(nombre) and len(nombre) >= 3:
                    array_nombres[i] = nombre
                    break
                else:
                    print("Error al ingresar un nombre incorrecto.")
    else:
        retorno = False
        
    return retorno

def cargar_votos(matriz_votos:list) -> bool:
    """Se encarga de cargar el nombre de los participantes.
    Args:
        matriz_votos (list): La lista donde se van a cargar los votos.
    Returns:
        bool: True si recibe como parametro una lista con valores. Sino False.
    """
    if type(matriz_votos) == list and len(matriz_votos) > 0:
        retorno = True
        for fil in range(len(matriz_votos)):
            for col in range(len(matriz_votos[fil])):
                mensaje = f"Ingrese el puntaje del participante {fil + 1} del jurado {col + 1}: "
                mensaje_error = "ERROR\nIngrese un número entre 1 y 10: "
                voto = ingresar_entero_rango(mensaje, mensaje_error, 1, 10)
                matriz_votos[fil][col] = voto
    else:
        retorno = False

    return retorno

def buscar_participante_por_nombre(array_nombres: list, matriz_notas: list, nombre: str) -> bool:
    """Busca un participante por su nombre y muestra su información si lo encuentra.
    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_notas (list): Matriz con los puntajes de los participantes.
        nombre (str): Nombre del participante a buscar.
    Returns:
        bool: Devuelve True si se encontró el participante. Sino False.
    """
    if es_alfabetico(nombre):
        bandera = False
        for fil in range(len(array_nombres)):
            if array_nombres[fil].lower() == nombre.lower():
                mostrar_voto(array_nombres, matriz_notas, fil)
                bandera = True
                return bandera
        
        return bandera
    else:
        print("Nombre inválido. Solo se permiten letras.")
        return bandera