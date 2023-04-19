from dictionary import*
from print import*
from algo1 import*
from ejercicios import*
import linkedlist
import math

print("")
print(""" - - - - Ejercicio 1 - - - - """)
print("")

"""
Ejemplificar que pasa cuando insertamos las llaves 5, 28, 19, 15, 20, 33, 12, 17, 10 en un HashTable con la colisión resulta por el método de chaining. Permita que la tabla tenga 9 slots y la función de hash: H (k) = k mod 9 
"""

dict = dictionary(9)
print("segun: H (k) = k mod 9")
KEYS = [5,28,19,15,20,33,12,17,10]
for i in KEYS:
  insert(dict,i,i)
  
print(" - - - - HASH TABLE - - - - ")
printHashtable(dict)
print(" - - - - - - - - - - - - - - ")

print("")
print(""" - - - - Ejercicio 2 - - - - """)
print("")

"""
Crear un módulo de nombre dictionary.py que implemente las siguientes especificaciones de las operaciones elementales para el TAD diccionario.
"""

dict = dictionary(11)
KEYS_VALUES = [(11,"Z"),(25,"R"),(33,"T"),(21,"X"),(37,"J"),(61,"H"),(66,"O"),(58,"C"),(53,"S"),(20,"K"),(79,"V"),(62,"L"),(77,"Q"),(88,"P"),(21,"B")]

for i in KEYS_VALUES:
  insert(dict,i[0],i[1])

KEYS = [11,37,61,96]
for i in KEYS:
  search(dict,i)

KEYS = [61,21,33,20]
for i in KEYS:
  delete(dict,i)

print(" - - - - HASH TABLE - - - - ")
printHashtable(dict)
print(" - - - - - - - - - - - - - - ")

print("")
print(""" - - - - Ejercicio 3 - - - - """)
print("")

"""
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves 61,62,63,64 y 65.
"""

print("segun: math.trunc(m*(k*A%1))")
L = [61,62,63,64,65]
for i in L:
  print("key:",Function_h2(i,1000))

print("")
print(""" - - - - Ejercicio 4 - - - - """)
print("")

"""
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
"""

S = ["federico","mendoza","abc","aaa"]
K = ["coridefe","mendoza","cba","aax"]

for i in range(0,len(S)):
  if IsPermutation(S[i],K[i]) == True:
    print("S es una permutacion de K")
  else:
    print("S NO es una permutacion de K")
    
print("")
print(""" - - - - Ejercicio 5 - - - - """)
print("")

"""
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución propuesta.
"""
  
L = [[1,2,3,4,5,6,7,8,9,10],[1,2,3],[0],[1,1]]

for i in L:
  if SingleElemt(i) == True:
    print("La lista tiene todos sus elementos unicos")
  else:
    print("La lista NO tiene elementos unicos")

print("")
print(""" - - - - Ejercicio 6 - - - - """)
print("")

"""
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar una función de hash apropiada para los códigos postales argentinos.
"""

L = ["C1024CWN","C0213XLLA","A0928OPCE"]
for i in L:
  print("Codigo postal:",i)
  print("Keys:",Function_h3(i,11))

print("")
print(""" - - - - Ejercicio 7 - - - - """)
print("")

"""
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta
"""
    
L = ["aabcccccaaa","aabccccca","abcd","a"]
for i in L:
  print("Palabra inicial:",i)
  print("Palabra resultado:",CharacterCounter(i))

print("")
print(""" - - - - Ejercicio 8 - - - - """)
print("")

"""
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta). Justificar el coste en tiempo de la solución propuesta.
"""
    
P = ["abracadacbra","patagonia","universo"]
A = ["cada","pata","aa"]
for i in range(0,len(P)):
  x = WordInWord(P[i],A[i])
  if x != None:
    print( x,", Indice de la primera ocurrencia de P dentro de A") 
  else:
    print("No se encuentra la palabra A dentro de P ")

print("")
print(""" - - - - Ejercicio 9 - - - - """)
print("")

"""
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
"""

S = [ [1,3,6,8] , [1,2,3,5] , [0,1,2,3,4,5] ]
T = [ [0,1,2,3,4,5,6,7,8,9] , [10,20,30,40,50,60,70,80,90] , [0,1,2] ]

for i in range(0,len(T)):
  if IsSubset(S[i],T[i]) == True:
    print("S ⊆ T (S es subconjunto de T)")
  else:
    print("S ⊆/ T (S NO es subconjunto de T)")