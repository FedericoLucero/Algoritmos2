# Ejercicio 7
def reduceLen(cadena):
    # Reduce la longitud de una cadena removiendo iterativamente pares de caracteres repetidos.
    i = 0
    while i < len(cadena):
        if cadena[i+1] == cadena[i]:
            cadena = cadena[0:i] + cadena[(i+2):]
        i = i + 1
    return cadena

# Ejercicio 8
def isContained(cadena, subcadena):
    # Determina si los caracteres de una cadena se encuentran contenidos y en el mismo orden dentro de otra cadena.
    cont = 0
    for char in cadena:
        if cont == len(subcadena):
            return True
        if char == subcadena[cont]:
            cont += 1
    else:
        return False

# Ejercicio 13
def Rhash(palabra):
    # Calcula el hash con potencia de 128
    num = 0
    pow = len(palabra) - 1
    for i in range(0, len(palabra)):
        num = num + (128 ** pow) * ord(palabra[i])
        pow = pow - 1
    return num

def rabin_karp(texto, patron):
    # Algoritmo de Rabin-Karp
    m = len(patron)
    n = len(texto)
    hash_patron = obtener_hash(patron)
    for i in range(0, n - m + 1):
        t_s = texto[i:i+m]
        if obtener_hash(t_s) == hash_patron and t_s == patron:
            print(patron, "encontrado en la posición", i)

def KMP(texto, patron):
    # Implementa el algoritmo KMP
    prefijos = calcular_funcion_prefijo(patron)
    ocurrencias = []
    q = 0  # caracteres macheados
    for i in range(len(texto)):
        while q > 0 and patron[q] != texto[i]:
            q = prefijos[q-1]  # no coincide, retrocede
        if patron[q] == texto[i]:
            q = q + 1  # el caracter coincide
        if q == len(patron):  # verifica que todo el patrón ha sido visto
            ocurrencias.append(i - len(patron) + 1)
            print("El patrón ocurre con desplazamiento", i - len(patron) + 1)
            q = prefijos[q-1]  # seguimos buscando
    return ocurrencias

def Compute_Prefix_Function(patron):
    # Calcula los mayores prefijos de P que son a la vez sufijos de Pq
    pi = [0] * len(patron)
    k = 0
    for q in range(1, len(patron)):
        while k > 0 and patron[k] != patron[q]:
            k = pi[k]
        if patron[k] == patron[q]:
            k += 1
        pi[q] = k
    return pi
