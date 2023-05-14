from algo1 import*
from ejercicios import*
import linkedlist
  
print("""Parte 1""")
print(" - - - - Ejercicio 1 - - - - ")

print("""G1 (simple, con ciclos, conexo, No completo)""")
ListV = [0,1,2,3]
ListA = [(0,1),(1,2),(2,3),(3,0)]
G1 = createGraph(ListV,ListA)
printGraph(G1)

print(" - - - - - - - - - - - - - - ")

print("""G2 (simple, con ciclos, No conexo, No completo)""")
ListV = [0,1,2,3,4,5,6]
ListA = [(0,1),(4,1),(1,2),(1,3),(2,3),(2,6)]
G2 = createGraph(ListV,ListA)
printGraph(G2)

print(" - - - - - - - - - - - - - - ")

print("""G3 (simple, sin ciclos ,conexo , No completo, arbol)""")
ListV = [0,1,2,3]
ListA = [(0,1),(1,2),(2,3)]
G3 = createGraph(ListV,ListA)
printGraph(G3)

print(" - - - - - - - - - - - - - - ")

print("""G4 (simple, con ciclos, conexo, completo)""")
ListV = [0,1,2,3]
ListA = [(0,1),(1,2),(2,3),(3,0),(2,0),(3,1)]
G4 = createGraph(ListV,ListA)
printGraph(G4)

"""lista de grafos"""
GraphList = [G1,G2,G3,G4]

print("")
print(" - - - - Ejercicio 2 - - - - ")
vertex1 = [1,1,0,0]
vertex2 = [2,5,3,2]

for i in range(0,len(vertex1)):
  if existPath(GraphList[i], vertex1[i], vertex2[i]) == True:
    print("Existe camino entre v1 y v2")
  else:
    print("NO Existe camino entre v1 y v2")
  print(" - - - - - - - - - - - - - - ")

print("")
print(" - - - - Ejercicio 3 - - - - ")

for G in GraphList:
  if isConnected(G) == True:
    print("Existe camino entre todo par de vértices")
  else:
    print("NO existe camino entre todo par de vértices")
  print(" - - - - - - - - - - - - - - ")

print("")
print(" - - - - Ejercicio 4 - - - - ")

for G in GraphList:
  if isTree(G) == True:
    print("El grafo es un árbol")
  else:
    print("El grafo NO es un árbol")
  print(" - - - - - - - - - - - - - - ")
  
print("")
print(" - - - - Ejercicio 5 - - - - ")
for G in GraphList:
  if isComplete(G) == True:
    print("El grafo es completo")
  else:
    print("El grafo NO es completo")
  print(" - - - - - - - - - - - - - - ")

print("")
print(" - - - - Ejercicio 6 - - - - ")

for G in GraphList:
  ListAristas = convertTree(G)
  if len(ListAristas) != 0:
    print("Las aristas que se pueden eliminar para que el grafo se convierta en un árbol:")
    print(ListAristas)
  else:
    print("El grafo ya es un arbol")
  print(" - - - - - - - - - - - - - - ")
  
print("")  

print("""Parte 2""")

print(" - - - - Ejercicio 7 - - - - ")

for G in GraphList:
  print("Cantidad de componentes conexas de G2:",countConnections(G))

print("")  
print(" - - - - Ejercicio 8 - - - - ")

ListV = [0,1,2,3,4,5]
ListA = [(0,3),(3,1),(3,2),(3,4),(4,5)]
print("Crea un grafo con class vertex()")
G5 = createGraph2(ListV,ListA)
printGraph2(G5)
print(" - - - - - - - - - - - - - ")
print("")
print("Grafo con la representación de Lista de Adyacencia con BFS, raiz 0")
printGraph2(convertToBFSTree(G5,0))

print(" - - - - Ejercicio 9 - - - - ")
ListV = [0,1,2,3,4,5]
ListA = [(0,3),(3,1),(3,2),(3,4),(4,5)]
print("Crea un grafo con class vertex()")
G6 = createGraph2(ListV,ListA)
printGraph2(G6)
print("Grafo con la representación de Lista de Adyacencia con DFS, raiz 0")
printGraph2(convertToDFSTree(G6,5))

print(" - - - - Ejercicio 10 - - - - ")
ListV = [0,1,2,3,4,5,6]
ListA = [(0,3),(3,1),(3,2),(3,4),(4,5),(0,6)]
print("Crea un grafo con class vertex()")
G7 = createGraph2(ListV,ListA)
printGraph2(G7)
print("Lista de vértices que representan el camino más corto entre v1 y v2")
print(bestRoad(G7, 5, 1))

"""
PRINT_PATH(G5,0,5)
"""