from dictionary import*
import math 

""" - - - - Ejercicio 3 - - - - """

"""
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves 61,62,63,64 y 65.
"""

def Function_h2(k,m):
  A = ((math.sqrt(5)-1)/2)
  return math.trunc(m*(k*A%1))

""" - - - - Ejercicio 4 - - - - """

"""
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
"""

def IsPermutation(S,P):
  length_S = len(S)
  if length_S == len(P):
    cont1 = 0 
    cont2 = 0
    for i in range(0,length_S):
      cont1 = cont1 + ord(S[i])
      cont2 = cont2 + ord(P[i])
    if cont1 == cont2:
      return True
  return False

""" - - - - Ejercicio 5 - - - - """

"""
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución propuesta.
"""

def SingleElemt(L):
  dict_5 = dictionary(11)
  for i in L:
    if search(dict_5,i) == True:
      return False
    else:
      insert(dict_5,i,i)
  return True
  
""" - - - - Ejercicio 6 - - - - """

"""
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar una función de hash apropiada para los códigos postales argentinos.
"""

def Function_h3(k,m):
  k0 = 0
  for i in k:
    if isinstance(i,int) == True:
      k0 = k0 + i
    else:
      k0 = k0 + ord(i)
  return (k0 % m)

""" - - - - Ejercicio 7 - - - - """

"""
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta
"""

def CharacterCounter(S):
  S_aux = S + " "
  comp = ""
  cont = 0
  c = S[0]
  for i in S_aux:
    if i != c:
      comp = comp + c
      comp = comp + str(cont)
      c = i
      cont = 0
    cont = cont + 1
  if len(S) <= len(comp):
    return S
  else:
    return comp
    
""" - - - - Ejercicio 8 - - - - """
      
"""
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta). Justificar el coste en tiempo de la solución propuesta.
"""

def SearchAndTraverse(A,i,dict,index):
  if i == len(A):
    return
  k = h(ord(A[i]),27)
  node = dict[k].head
  while node != None:
    if index + 1 == node.value[1][1]:
      SearchAndTraverse(A,i+1,dict,index+1)
      return True
    node = node.nextNode
  return False

def WordInWord(P,A):
  if len(P) > len(A):
    dict = dictionary(27)
    cont = 0
    for i in P:
      insert(dict,ord(i),[i,cont])
      cont = cont + 1

    k = h(ord(A[0]),27)
    if dict[k] != None:
      node = dict[k].head
      while node != None:
        index = node.value[1][1]
        if SearchAndTraverse(A,1,dict,index) == True:
          return index
        node = node.nextNode
    
""" - - - - Ejercicio 9 - - - - """

"""
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
"""

def IsSubset(S,T):
  dict_9_1 = dictionary(11)
  for i in T:
    insert(dict_9_1,i,i)
  for i in S:
    if search(dict_9_1,i) == None:
      return False
  return True