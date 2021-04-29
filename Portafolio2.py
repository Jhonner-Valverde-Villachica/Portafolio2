# Portafolio #2.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio #1.
# Invertir los elementos de una lista.

"""
Nombre: invertirLista
Entradas: Recibir una lista con elementos.
Salidas: Invertir los elementos de una lista.
Restricciones: Si la lista está vacía, devolver 0.
"""

def contarDigitos(num):
    if(isinstance(num, int) == False):
        return print("Error tipo de dato, no es entero.")
    elif (num == 0):
        return 1
    else:
        return contarDigitos_aux(num, 0)

def contarDigitos_aux(n, resultado):
    if(n == 0):
        return resultado
    else:
        return contarDigitos_aux(n // 10, resultado + 1)

def invertirLista(lista):
    if lista == []:
        if lista == []:
            return 0
        else:
            return invertirLista_Aux(lista, contarDigitos(num))
    else:
        return print("Error: Tipo de dato.")
    
def invertirLista_Aux(lista, largo):
    if largo == 0:
        return 0
    else:
        return invertirLista_Aux((lista // 10, [-1]) + (num % 10) * (10 ** ([-1] - 1)))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio #2.
# Determinar cuál es el número menor y mayor de una lista.

"""
Nombre: extremosLista
Entradas: Recibir una lista con elementos.
Salidas: Determinar cuál es el número menor y mayor de una lista.
Restricciones: Si la lista está vacía devolver “error”.
"""

def extremosLista(lista):
    if lista == []:
        if lista == []:
            return print("error")
        else:
            extremosLista_Aux(lista, menor, mayor)
    else:
        return print("Error: Tipo de dato no es válido.")

def extremosLista_Aux(lista, subLista, menor, mayor):
    if lista == [] and subLista == []:
        return 0
    elif lista and subLista:
        return extremosLista_Aux(lista [:], subLista [:], menor, mayor)
    else:
        return extremosLista2_Aux(lista2, subLista2, menor2, mayor2)

def extremosLista2_Aux(lista2, subLista2, menor2, mayor2):
    if (lista2 [:]) and (subLista2 [:]):
        lista2 == menor2
        subLista2 == mayor2
        if lista2 and subLista2:
            return extremosLista2_Aux(lista2 [:], sublista2 [:], menor, mayor)
        else:
            return extremosLista2_Aux(lista2 [:], subLista2 [:], menor + 1, mayor + 1)
    else:
        if lista2 and subLista2:
            return extremosLista2_Aux(lista2 [1:], subLista2 [1:], menor, mayor)
        else:
            return extremosLista2_Aux(lista2 [:], subLista2 [:], menor - 1, mayor + 1)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio #3.
# Sacar dígitos de un número.

"""
Nombre: eliminarDigito
Entradas: Recibir dos tipos de datos numéricos.
          num1 == Numeración cualquiera.
          num2 == Número indicado o Números indicados a eliminar en num1.
Salidas: Eliminar el dígito que se indique en num2 y retornar un nuevo número teniendo como base num1, a raiz de la eliminación de lo indicado en num2.
Restricciones: Si el número es "Cero", devolver el mensaje correspondiente al "error".
"""

def eliminarDigito(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        if num1 == 0 and num2:
            return print("error")
        else:
            return eliminarDigito_Aux(num1, num2, analizar, eliminar)
    else:
        return print("Error: Datos no son enteros.")

def eliminarDigito_Aux(num1, num2, analizar, eliminar):
    num1 == analizar
    num2 == eliminar
    if num1 and num2:
        if num1 and num2:
            return eliminarDigito_Aux(num1 // 10, num2 - num1, analizar, eliminar)
        else:
            return eliminarDigito_Aux(num1, num2, analizar + 1, eliminar - 1)
    else:
        return eliminarDigito2_Aux(num1V2, num2V2, analizar, eliminar)

def eliminarDigito2_Aux(num1V2, num2V2, analizar, eliminar):
    num1 == analizar
    num2 == eliminar
    if num1V2 and num2V2:
        if num1V2 == [] and num2V2 == []:
            return eliminarDigito2_Aux(num1V2 [:] // 10, num2V2, analizar, eliminar)
        else:
            return eliminarDigito2_Aux(num1V2 [:] // 10, num2V2, analizar, eliminar - 1)
    else:
        if num1V2 and num2V2:
            return eliminarDigito2_Aux(num1V2 [:] // 10, num2V2 [:] - num2V2, analizar, eliminar)
        else:
            return eliminarDigito2_Aux(num1V2 [:] // 10, num2V2 [:] - num2V2, analizar, eliminar - 1)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio #4.
# Determinar subListas.

"""
Nombre: nivelesLista
Entradas: Ingresar listas de listas.
Salidas: Retornar una lista de listas y la cantidad de sublistas que lo contiene.
Restricciones: Solo se permiten listas.
"""

def nivelesLista(lista1, lista2, lista3):
    lista1 == []
    lista2 == []
    lista3 == []
    if lista1 == [] and lista2 == [] and lista3 == []:
        if lista1 and lista2 and lista3:
            return print("0, 0, 0")
        else:
            return nivelesLista_Aux(lista1, lista2, lista3, promedio)
    else:
        return print("Error: Tipo de dato inválido")

def nivelesLista_Aux(lista1, lista2, lista3, promedio):
    if (lista1 and lista2 and lista3) == promedio:
        if lista1 and lista2 and lista3:
            return nivelesLista_Aux(lista1, lista2, lista3, promedio)
        else:
            return nivelesLista_Aux(lista1 [:], lista2 [:], lista3 [:], promedio)
    else:
        return nivelesLista2_Aux(lista1, lista2, lista3, promedio, cont)

def nivelesLista2_Aux(lista1, lista2, lista3, promedio, cont):
    if (lista1 and lista2 and lista3) == promedio:
        if lista1 and lista2 and lista3:
            if promedio:
                return nivelesLista2_Aux(lista1 [:] // [], lista2 [:] // [], lista3 [:] // [], cont - 1)
            elif promedio == (lista1 and lista2 and lista3):
                return nivelesLista2_Aux(lista1 [1:] // [], lista2 [1:] // [], lista3 [1:] // [], cont - 1)
            elif promedio == (lista1 and lista2 and lista3):
                return nivelesLista2_Aux(lista1 [1:] // [], lista2 [1:] // [], lista3 [1:] // [], cont + 1)
            else:
                return nivelesLista2_Aux(lista1 [:] // [], lista2 [:] // [], lista3 [:] // [], cont + 1)
        else:
            return print("Error: No cumple con los parámetros de entrada")
    else:
        if (lista1 and lista2 and lista3) ==+ promedio:
            return nivelesLista2_Aux((lista1 [:] // [], lista2 [:] // [], lista3 [:] // [], cont + 1) // [])
        else:
            return print("Error: Ningún elemeneto es válido")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio #5.
# Retornar Indices de vectores.

"""
Nombre: obtenerIndicesListaVectore
Entradas: Una lista de vectores.
Salidas: Devolver los índices de una lista de vectores cuyo valor sean cero o un número negativo.
Restricciones: Los valores de las listas deben ser únicamente cero un número negativo.
"""

v1 = [12, 56, 0, 0, -8, 3]
v2 = [-26, 2, 75, 0, -18, 0]
v3 = [6, 2, 7, 10, 50, 90]

def obtenerIndicesListaVectore(v1, v2, v3):
    if isinstance(v1, list) and (v2, list) and (v3, list):
        if v1 and v2 and v3:
            return obtenerIndicesListaVectore_Aux((v1, v2, v3) - 1)
        else:
            return obtenerIndicesListaVectore_Aux(v1, v2, v3, promedio, cont)
    else:
        return print("Error: Tipo de dato inválido")

def obtenerIndicesListaVectore_Aux(v1, v2, v3, promedio, cont):
    if (v1, v2, v3) == promedio:
        if (v1, v2, v3) // 10:
            return obtenerIndicesListaVectore_Aux(v1, v2, v3, promedio, cont - 1)
        else:
            return obtenerIndicesListaVectore2_Aux(v1, v2, v3, buscar, analizar)

def obtenerIndicesListaVectore2_Aux(v1, v2, v3, buscar, analizar):
    buscar = v1, v2, v3
    analizar = 0
    if (v1, v2, v3):
        return obtenerIndicesListaVectore2_Aux((v1, v2, v3) + count, [], - 1)
    else:
        return obtenerIndicesListaVectore2_Aux(v1, v2, v3, buscar, analizar)
