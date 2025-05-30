
def crear_array(cantidad_elementos:int, valor_inicial:any) -> list:
    """Se encarga de crear una matriz con los parametros asignados.
    Args:
        cantidad_elementos (int): Cantidad de elementos de la nueva lista.
        valor_inicial (any): Valor de cada elemento en cada fila.
    Returns:
        list: Retorna una nueva lista creada.
    """
    array = [valor_inicial] * cantidad_elementos
    return array

def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    """Se encarga de crear una matriz con los parametros asignados.
    Args:
        cantidad_filas (int): Cantidad de filas de la nueva matriz.
        cantidad_columnas (int): Cantidad de columnas de la nueva matriz.
        valor_inicial (any): Valor de cada elemento en cada fila.
    Returns:
        list: Retorna una nueva matriz creada.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def mostrar_array(array:list) -> None:
    """Se encarga de mostrar el nombre de los participantes en la consola.
    Args:
        array (list): Lista que se va mostrar.
    Returns:
        None: No devuelve nada, solo imprime una lista en consola.
    """
    for i in range(len(array)):
        print(f"{array[i]}")

def mostrar_matriz(matriz:list) -> None:
    """Se encarga de mostrar los votos de los participantes en la consola.
    Args:
        matriz (list): Matriz que se va mostrar.
    Returns:
        None: No devuelve nada, solo imprime una matriz en consola.
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}",end=" ")
        print("")

def calcular_porcentaje(cantidad_total:int|float, cantidad_parcial:int|float) -> float | None:
    """Calcula el porcentaje entre la cantidad total y la cantidad parcial.
    Args:
        cantidad_total (int|float): Int o float de la cantidad total.
        cantidad_parcial (int|float): Int o float de la cantidad parcial.
    Returns:
        float | None: Devuelve un float si la cantidad total es diferente a 0. Sino devuelve None.
    """
    if cantidad_total != 0:
        porcentaje = cantidad_parcial * 100 / cantidad_total
    else:
        porcentaje = None
        
    return porcentaje

def sumar_matriz(matriz_numerica:list) -> int | float:
    """Suma total de la matriz.
    Args:
        matriz_numerica (list): Matriz con votos.
    Returns:
        int | float: Devuelve el resultado de la suma total de la matriz.
    """
    suma = 0
    for fil in range(len(matriz_numerica)):
        for col in range(len(matriz_numerica[fil])):
            if type(matriz_numerica[fil][col]) == int or type(matriz_numerica[fil][col]) == float:
                suma += matriz_numerica[fil][col]
                
    return suma

def sumar_fila(matriz_numerica:list, indice_fila:int) -> int | float:
    """Suma la fila de la matriz del primer argumento.
    Args:
        matriz_numerica (list): Matriz con votos.
        indice_fila (int): Indice de la fila.
    Returns:
        int | float: Devuelve el resultado de la suma de la fila indicada.
    """
    suma_fila = 0
    for col in range(len(matriz_numerica[0])):
        if type(matriz_numerica[indice_fila][col]) == int or type(matriz_numerica[indice_fila][col]) == float :
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila

def mostrar_voto(array_nombres:list, matriz_votos:list, indice:int) -> bool:
    """Calcula el porcentaje entre la cantidad total y la cantidad parcial.
    Args:
        array_nombres (list): Lista con nombres de los participantes.
        matriz_votos (list): Matriz de votos a mostrar.
        indice (int): Indice.
    Returns:
        bool: Devuelve True si recibe una matriz con votos, una lista con nombres y un indice mayor a 0. Sino false.
    """
    if type(matriz_votos) == list and type(array_nombres) == list and len(matriz_votos) > 0 and len(array_nombres) > 0 and (indice < len(array_nombres) and indice >= 0):
        promedio = calcular_promedio_votos(matriz_votos, indice)
        retorno = True
        print(f"PARTICIPANTE: {array_nombres[indice]}")
        print(f"PUNTAJE JURADO 1: {matriz_votos[indice][0]}")
        print(f"PUNTAJE JURADO 2: {matriz_votos[indice][1]}")
        print(f"PUNTAJE JURADO 3: {matriz_votos[indice][2]}")
        print(f"PUNTAJE PROMEDIO: {round(promedio,2)}/10 ")
    else:
        retorno = False
        
    return retorno

def calcular_promedio_votos(matriz_votos: list, indice: int) -> float:
    """Calcula el promedio de votos de un participante.
    Args:
        matriz_votos (list): Matriz de votos a mostrar.
        indice (int): Indice.
    Returns:
        float: Devuelve el número promedio de un participante.
    """
    acumulador = sumar_fila(matriz_votos, indice)
    contador = len(matriz_votos[indice])
    promedio = calcular_promedio(acumulador, contador)
    return promedio

def calcular_promedio(acumulador:float | int, contador:int) -> float | None:
    """Calcula el promedio entre los datos recibidos.
    Args:
        acumulador (float | int): Suma de todos los valores.
        contador (int): Entre cuantos se va dividir.
    Returns:
        float | None: Devuelve el valor promedio entre los argumentos dados.
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
    return promedio

def mostrar_votos(array_nombres:list, matriz_votos:list) -> bool:
    """Calcula el porcentaje entre la cantidad total y la cantidad parcial.
    Args:
        array_nombres (list): Lista con nombres de los participantes.
        matriz_votos (list): Matriz de votos a mostrar.
    Returns:
        bool: Devuelve True si recibe una matriz con votos, una lista con nombres mayor a 0. Sino false.
    """
    if type(matriz_votos) == list and type(array_nombres) == list and len(matriz_votos) > 0 and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            mostrar_voto(array_nombres,matriz_votos,i)
            print("")
    else:
        retorno = False
        
    return retorno

def ingresar_entero(mensaje:str) -> int:
    """Mensaje que pide un valor de entrada y lo valida.
    Args:
        mensaje (str): Mensaje que va ver el usuario antes de pedir un valor de entrada.
    Returns:
        int: Devolvemos un entero después de validar su valor.
    """
    numero = input(mensaje)
    
    while not es_entero(numero):
        print("ERROR NO ES UN NUMERO")
        numero = input(mensaje)
    
    numero = int(numero)
    
    return numero

def ingresar_entero_rango(mensaje:str, mensaje_error:str, minimo:int, maximo:int) -> int:
    """Solicita al usuario un número entero dentro de un rango específico y lo valida.
    Args:
        mensaje (str): Mensaje a mostrar para solicitar el número inicialmente.
        mensaje_error (str): Mensaje a mostrar si el número está fuera del rango.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.
    Returns:
        int: Número entero ingresado dentro del rango válido.
    """
    numero = ingresar_entero(mensaje)
    while numero > maximo or numero < minimo:
        numero = ingresar_entero(mensaje_error)
    return numero
    
def es_entero(cadena:str) -> bool:
    """Valida si la cadena de caracteres esta compuesta por numeros de 0 a 9.
    Args:
        cadena (str): Cadena de caracteres de 0 a 9.
    Returns:
        bool: Devuelve True si la cadena de caracteres no esta vacía. Sino False.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

def es_alfabetico(cadena:str) -> bool:
    """Verifica si una cadena contiene solo letras (sin espacios ni caracteres especiales).
    Args:
        cadena (str): Cadena de texto a validar.
    Returns:
        bool: Devuelve True si la cadena contiene solo letras. Sino False.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if (valor_ascii > 90 or valor_ascii < 65) and (valor_ascii > 122 or valor_ascii < 97):
                retorno = False
                break
    else:
        retorno = False 
    
    return retorno

def mostrar_participantes_no_superan_puntaje_promedio(array_nombres:list, matriz_notas:list, promedio:float) -> bool:
    """ Muestra los participantes que su puntaje promedio es menor al valor promedio ingresado.
    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_notas (list): Matriz con las notas de cada participante (una fila por participante).
        promedio (float): Puntaje de referencia para comparar.
    Returns:
        bool: True si se encontró al menos un participante con promedio menor al valor dado. Sino False.
    """
    bandera = False
    for fil in range(len(matriz_notas)):
        suma_puntaje = sumar_fila(matriz_notas, fil)
        contador = len(matriz_notas[0])
        promedio_puntaje = calcular_promedio(suma_puntaje, contador)

        if promedio_puntaje < promedio:
            mostrar_participante(array_nombres, matriz_notas, fil)
            print("")
            bandera = True
    return bandera

def mostrar_participante(lista_nombres:list, matriz_notas:list, indice:int) -> None:
    """ Muestra un participante con un indice específico.
    Args:
        lista_nombres (list): Lista con los nombres de los participantes.
        matriz_notas (list): Matriz con los puntajes.
        indice (int): Indice para ingresar al valor correspondiente.
    Returns:
        None: No devuelve nada, solo imprime una lista en consola.
    """
    print(f"Nombre: {lista_nombres[indice]}")
    for col in range(len(matriz_notas[0])):
        print(f"PUNTAJE JURADO {col + 1}: {matriz_notas[indice][col]}")

def mostrar_participantes(lista_nombres:list, matriz_notas:list) -> None:
    """ Muestra una lista de participantes.
    Args:
        lista_nombres (list): Lista con los nombres de los participantes.
        matriz_notas (list): Matriz con los puntajes.
    Returns:
        None: No devuelve nada, solo imprime una lista en consola.
    """
    for i in range(len(lista_nombres)):
        print(f"MOSTRANDO PARTICIPANTE {i + 1}")
        mostrar_participante(lista_nombres, matriz_notas, i)
        print("")

def mostrar_promedio_por_jurado(matriz_notas: list) -> None:
    """ Muestra el promedio de puntajes otorgados por cada jurado.
    Args:
        matriz_notas (list): Matriz con los puntajes.
    Returns:
        None: No devuelve nada, solo imprime una lista en consola.
    """
    cantidad_jurados = len(matriz_notas[0])
    cantidad_participantes = len(matriz_notas)
    for col in range(cantidad_jurados):
        suma = 0
        for fil in range(cantidad_participantes):
            suma += matriz_notas[fil][col]
        promedio = calcular_promedio(suma, cantidad_participantes)
        print(f"PROMEDIO DEL JURADO {col + 1}: {round(promedio, 2)}/10")

def mostrar_jurado_mas_estricto(matriz_notas: list) -> None:
    """ Determina y muestra cuál jurado otorgó los puntajes promedio más bajos.
    Args:
        matriz_notas (list): Matriz con los puntajes de los participantes por jurado.
    Returns:
        None: No devuelve nada, solo imprime una lista en consola.
    """
    cantidad_jurados = len(matriz_notas[0])
    cantidad_participantes = len(matriz_notas)
    
    jurado_mas_estricto = -1
    promedio_mas_bajo = float('inf')

    for col in range(cantidad_jurados):
        suma = 0
        for fil in range(cantidad_participantes):
            suma += matriz_notas[fil][col]
        
        promedio = calcular_promedio(suma, cantidad_participantes)

        if promedio < promedio_mas_bajo:
            promedio_mas_bajo = promedio
            jurado_mas_estricto = col
    
    print(f"El jurado más estricto fue el número {jurado_mas_estricto + 1} con un promedio de {round(promedio_mas_bajo, 2)}/10.")

def mostrar_jurado_mas_generoso(matriz_notas: list) -> None:
    """ Calcula y muestra cuál jurado otorgó los puntajes promedio más altos.
    Args:
        matriz_notas (list): Matriz con los puntajes de los participantes por jurado.
    Returns:
        None: No devuelve nada, solo imprime una lista en consola.
    """
    indice_mas_generoso = 0
    promedio_mas_alto = 0
    cantidad_participantes = len(matriz_notas)
    cantidad_jurados = len(matriz_notas[0])
    for col in range(cantidad_jurados):
        suma_columna = 0
        for fil in range(cantidad_participantes):
            suma_columna += matriz_notas[fil][col]
        
        promedio = calcular_promedio(suma_columna, cantidad_participantes)

        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            indice_mas_generoso = col

    print(f"El jurado más generoso fue el número {indice_mas_generoso + 1} con un promedio de {round(promedio_mas_alto, 2)} puntos.")

def mostrar_participantes_puntajes_iguales(array_nombres: list, matriz_notas: list) -> bool:
    """ Muestra los participantes que recibieron la misma puntuación de todos los jurados.
    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_notas (list): Matriz con los puntajes de los participantes por jurado.
    Returns:
        bool: Devuelve True si hay al menos un participante con puntajes iguales. Sino False.
    """
    bandera = False
    for fil in range(len(matriz_notas)):
        primer_nota = matriz_notas[fil][0]
        es_igual = True

        for col in range(1, len(matriz_notas[fil])):
            if matriz_notas[fil][col] != primer_nota:
                es_igual = False
                break

        if es_igual:
            print(f"PARTICIPANTE: {array_nombres[fil]}")
            print(f"PUNTAJES: {matriz_notas[fil]}")
            print("")
            bandera = True

    return bandera

def ordenar_participantes_alfabeticamente(array_nombres:list, matriz_notas:list) -> None:
    """Ordena alfabeticamente nombres dentro de una lista.
    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_notas (list): Matriz con los puntajes de los participantes.
    Returns:
        None: No tiene retorno.
    """
    for izq in range(len(array_nombres) - 1):
        for der in range(izq + 1, len(array_nombres)):
            if array_nombres[izq].lower() > array_nombres[der].lower():
                intercambiar_indices(array_nombres, izq, der)
                intercambiar_indices(matriz_notas, izq, der)

def intercambiar_indices(array:list, izq:int, der:int) -> None:
    """ Intercambia dos elementos de un array.
    Args:
        array (list): Lista con los nombres de los participantes.
        izq (int): Valor izquierda.
        der (int): Valor derecha.
    Returns:
        None: No tiene retorno.
    """
    aux_izq = array[izq]
    array[izq] = array[der]
    array[der] = aux_izq