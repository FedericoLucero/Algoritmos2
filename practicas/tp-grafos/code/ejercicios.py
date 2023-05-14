import linkedlist
from algo1 import*
"""Parte 1"""

"""primer tipo de grafo con nodos == numero"""

def Graph(n):
  G = Array(n,linkedlist.LinkedList())
  return G

#O(V+A)
def printGraph(G):
  for i in range(0,len(G)):
    if G[i] == None:
      print("[",G[i],"]")
    else:
      currentNode = G[i].head
      while currentNode!= None:
        print("[",currentNode.value,"] ",end = " ")
        currentNode = currentNode.nextNode
      print(" ")

"""Ejercicio 1"""
"""
def createGraph(List,List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
"""
#O(A+V)
def createGraph(ListV, ListA):
  n = len(ListV)
  G = Graph(n)
  for i in range(0,n):
    G[i] = linkedlist.LinkedList()
    linkedlist.add(G[i],ListV[i])
  for i in ListA:
    linkedlist.insert(G[i[0]], i[1],1)
    linkedlist.insert(G[i[1]], i[0],1)
  return G 
  
"""Ejercicio 2"""
"""
def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
"""
#O(v^2)
def existPath(Grafo, v1, v2):
  firstList = Grafo[v1]
  auxList = [v1]
  return existPathR(Grafo, firstList, auxList, v2)
    
def existPathR(Grafo, List, auxList, v2):
  if linkedlist.search(List,v2) != None:
    return True
  currentNode = List.head
  condition = False
  while currentNode != None:
    if currentNode.value not in auxList:
      auxList.append(currentNode.value)
      condition = existPathR(Grafo, Grafo[currentNode.value], auxList, v2)
    if condition == True:
      return condition
    currentNode = currentNode.nextNode
  return False
  
"""Ejercicio 3"""
"""
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
"""
#O(V+A)
def isConnected(Grafo):
  auxList = []
  Vertex = []
  for i in range(0,len(Grafo)):
    Vertex.append(Grafo[i].head.value)
    currentNode = Grafo[i].head.nextNode
    while currentNode != None:
      if currentNode.value not in auxList:
        auxList.append(currentNode.value)
      currentNode = currentNode.nextNode
  auxList.sort()
  if auxList != Vertex:
    return False
  else:
    return True

"""Ejercicio 4"""
"""
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
"""
#O(A+V)
def isTree(Grafo):
  #contar aristas (aristas == vertices - 1)
  #detectar bucles
  #(en este caso con ver que sea conexo y cumpla aristas == vertices-1 basta)
  if len(Grafo)-1 == countConnections(Grafo):
    return isConnected(Grafo)
  return False
  
"""Ejercicio 5"""
"""
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.
Nota: Tener en cuenta que  un grafo es completo cuando existe una arista entre todo par de vértices.
"""
#O(A+V)
def isComplete(Grafo):
  n = len(Grafo)
  if n*(n-1)/2 == countConnections(Grafo):
    return True
  return False
  
"""Ejercicio 6"""
"""
def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
"""
#O(A+V)
def convertTree(Grafo):
  Aristas = returnConnections(Grafo)
  aux=[]
  list=[]
  for i in range(0,len(Aristas)):
    if Aristas[i][1] not in aux:
      aux.append(Aristas[i][1])
    else:
      list.append(Aristas[i])
  return(list)
#O(A+V)
def returnConnections(Grafo):
  aux = []
  for i in range(0,len(Grafo)):
    currentNode = Grafo[i].head.nextNode
    while currentNode != None:
      x = (Grafo[i].head.value,currentNode.value)
      if x and x[::-1] not in aux:
        aux.append(x)
      currentNode = currentNode.nextNode
      #print(aux)
  return aux

"""Parte 2"""

"""Ejercicio 7"""
"""
def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
"""
#O(A+V)
def countConnections(Grafo):
  aux = []
  for i in range(0,len(Grafo)):
    currentNode = Grafo[i].head.nextNode
    while currentNode != None:
      x = (Grafo[i].head.value,currentNode.value)
      if x and x[::-1] not in aux:
        aux.append(x)
      currentNode = currentNode.nextNode
      #print(aux)
  return len(aux)

"""sugundo tipo de grafo con nodos == vertex , elemento == nodos.value"""
#para que sea mas facil inicializar (value,)
class Vertex:
  value = None
  color = None
  d = None
  pi = None
  f = None

def createGraph2(ListV, ListA):
  n = len(ListV)
  GV = Graph(n)
  for i in range(0,n):
    nodo = Vertex()
    nodo.value = ListV[i]
    GV[i] = linkedlist.LinkedList()
    linkedlist.add(GV[i],nodo)
  for i in ListA:
    linkedlist.insert(GV[i[0]], GV[i[1]].head.value,1)
    linkedlist.insert(GV[i[1]], GV[i[0]].head.value,1)
  return GV

def printGraph2(G):
  if G == None:
    return
  for i in range(0,len(G)):
    if G[i] == None:
      print("[",G[i],"]")
    else:
      currentNode = G[i].head
      while currentNode!= None:
        print("[",currentNode.value.value,"] ",end = " ")
        currentNode = currentNode.nextNode
      print(" ")
      
"""Ejercicio 8"""
"""
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
"""
#O(A+V)
def convertToBFSTree(Grafo, v): # v = s (para guia en la teoria)
  n = len(Grafo) 
  for i in range(0,n): # inicializo los vertex (con inicializar los head de las listas ya se inician todos)
    nodo_u = Grafo[i].head.value # nodo vertex u
    nodo_u.color = "White"
    #nodo_u.d = "Infinit"
  
    nodo_u.pi = "Nil"
  nodo_v = Grafo[v].head.value # nodo vertex v
  nodo_v.color = "Gray"
  #nodo_v.d = 0
  nodo_v.pi = "Nil"
  Q = []
  Q.append(nodo_v) # -> []
  ###
  aux = []
  ###
  while len(Q) != 0:
    nodo_u = Q.pop() # [] -> (primero en entrar primero en salir)
    #print(nodo_u.value)
    currentNode = Grafo[nodo_u.value].head # currentNode de la likedlist
    while currentNode != None:
      nodo_w = currentNode.value
      if nodo_w.color == "White":
        nodo_w.color = "Gray"
        #nodo_w.d = nodo_u.d + 1
        nodo_w.pi = nodo_u
        ###
        arista = (nodo_w.value,nodo_u) # arista = tupla de vertices
        if arista and arista[::-1] not in aux: # crea una lista de aristas sobrantes (Arcos de retroceso)
          aux.append(arista)
        ###
        Q.append(nodo_w)
      currentNode = currentNode.nextNode
    nodo_u.color = "Black"
  ###
  for i in aux: # elimina de el grafo las aristas sobrantes (Arcos de retroceso)
    linkedlist.delete(Grafo[i[0]],i[1])
    
  return Grafo
  ###
"""Ejercicio 9"""
"""
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
"""
#O(V+A)
def convertToDFSTree(Grafo, v):
  n = len(Grafo) 
  for i in range(0,n): # inicializo los vertex (con inicializar los head de las listas ya se inician todos)
    nodo_u = Grafo[i].head.value # nodo vertex u
    nodo_u.color = "White" 
    #nodo_u.pi = "Nil"
  time = 0
  ###
  aux = []
  DFS_Visit(Grafo,v,time,aux) # para que la que la raiz sea v
  ###
  for i in range(0,n): # por si no es conexo
    nodo_u = Grafo[i].head.value
    if nodo_u.color == "White":
      DFS_Visit(Grafo,nodo_u.value,time,aux)
  ###
  for i in aux: # elimina de el grafo las aristas sobrantes (Arcos de retroceso)
    linkedlist.delete(Grafo[i[0]],i[1])
  return Grafo
  ###

def DFS_Visit(Grafo,u,time,aux):
  #time = time + 1
  nodo_u = Grafo[u].head.value
  #nodo_u.d = time
  nodo_u.color = "Gray"
  #print(nodo_u.value)
  currentNode = Grafo[nodo_u.value].head # currentNode de la likedlist
  while currentNode != None:
    nodo_w = currentNode.value
    if nodo_w.color == "White":
      #nodo_w.pi = nodo_u
      ###
      arista = (nodo_w.value,nodo_u) # arista = tupla de vertices
      if arista and arista[::-1] not in aux: # crea una lista de aristas sobrantes (Arcos de retroceso)
        aux.append(arista)
      ###
      DFS_Visit(Grafo,nodo_w.value,time,aux)  
    currentNode = currentNode.nextNode
  nodo_u.color = "Black"
  #time = time +1
  #nodo_u.f = time
  
"""Ejercicio 10"""
"""
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
"""
#O(V+A)
def bestRoad(Grafo, v1, v2):
  n = len(Grafo) 
  for i in range(0,n): # inicializo los vertex (con inicializar los head de las listas ya se inician todos)
    nodo_u = Grafo[i].head.value # nodo vertex u
    nodo_u.color = "White"
    nodo_u.pi = "Nil"
  nodo_v = Grafo[v2].head.value # nodo vertex v
  nodo_v.color = "Gray"
  nodo_v.pi = "Nil"
  Q = []
  Q.append(nodo_v) # -> []

  while len(Q) != 0:
    nodo_u = Q.pop() # [] -> (primero en entrar primero en salir)
    currentNode = Grafo[nodo_u.value].head # currentNode de la likedlist
    while currentNode != None:
      nodo_w = currentNode.value
      if nodo_w.color == "White":
        nodo_w.color = "Gray"
        nodo_w.pi = nodo_u
        ###
        if nodo_w.value == v1:
          return TraverseToRoot(nodo_w)
        ###
        Q.append(nodo_w)
      currentNode = currentNode.nextNode
    nodo_u.color = "Black"
  return []

def TraverseToRoot(nodo):
  aux = []
  while nodo.pi != "Nil":
    aux.append(nodo.value)
    nodo = nodo.pi
  aux.append(nodo.value)
  return aux


"""
def PRINT_PATH(G,s,v):
  nodo_s = G[s].head.value
  nodo_v = G[v].head.value
  if  nodo_v.value == nodo_s.value:
    print(nodo_s.value)
  else:
    if nodo_v.pi == "Nil":
      print("no path from", nodo_s.value ,"to",nodo_v.value, "exists")
    else:
      PRINT_PATH(G, nodo_s.value, nodo_v.pi.value)
      print(nodo_v.value)
"""

"""Ejercicio 11 (Opcional)"""
"""
def isBipartite(Grafo): 
Descripción: Implementa la operación es bipartito
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es bipartito.
NOTA: Un grafo es bipartito si no tiene ciclos de longitud impar.
"""

"""Ejercicio 12"""
"""
Demuestre que si el grafo G es un árbol y se le agrega una arista nueva entre cualquier par de vértices se forma exactamente un ciclo y deja de ser un árbol.
Ejercicio 13
Demuestre que si la arista (u,v) no pertenece al árbol BFS, entonces los niveles de u y v difieren a lo sumo en 1.
"""

"""Parte 3"""

"""Ejercicio 14"""
"""
def PRIM(Grafo): 
Descripción: Implementa el algoritmo de PRIM 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo
"""

"""Ejercicio 15"""
"""
def KRUSKAL(Grafo): 
Descripción: Implementa el algoritmo de KRUSKAL 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo
"""

"""Ejercicio 16"""
"""
Demostrar que si la arista (u,v) de costo mínimo tiene un nodo en U y otro en V - U, entonces la arista (u,v) pertenece a un árbol abarcador de costo mínimo.
"""

"""Parte 4"""

"""Ejercicio 17"""
"""
Sea e la arista de mayor costo de algún ciclo de G(V,A) . Demuestre que existe un árbol abarcador de costo mínimo AACM(V,A-e) que también lo es de G.
"""

"""Ejercicio 18"""
"""
Demuestre que si unimos dos AACM por un arco (arista) de costo mínimo el resultado es un nuevo AACM. (Base del funcionamiento del algoritmo de Kruskal)
"""

"""Ejercicio 19"""
"""
Explique qué modificaciones habría que hacer en el algoritmo de Prim sobre el grafo no dirigido y conexo G(V,A), o sobre la función de costo c(v1,v2)-> R para lograr: 	
1. Obtener un árbol de recubrimiento de costo máximo. 		
2. Obtener un árbol de recubrimiento cualquiera.
3. Dado un conjunto de aristas E ∈ A, que no forman un ciclo, encontrar el árbol de recubrimiento mínimo Gc(V,AC) tal que E ∈ Ac.
"""

"""Ejercicio 20"""
"""
Sea G<V, A> un grafo conexo, no dirigido y ponderado, donde todas las aristas tienen el mismo costo. Suponiendo que G está implementado usando matriz de adyacencia, haga en pseudocódigo un algoritmo O(V2) que devuelva una matriz M de VxV donde: M[u, v] = 1 si (u,v) ∈ A y (u, v) estará obligatoriamente en todo árbol abarcador de costo mínimo de G, y cero en caso contrario.
"""
"""Parte 5"""

"""Ejercicio 21"""
"""
Implementar el Algoritmo de Dijkstra que responde a la siguiente especificación
def shortestPath(Grafo, s, v): 
Descripción: Implementa el algoritmo de Dijkstra
Entrada: Grafo con la representación de Matriz de Adyacencia, vértice de inicio s y destino v.
Salida: retorna la lista de los vértices que conforman el camino iniciando por s y terminando en v. Devolver NONE en caso que no exista camino entre s y v.
"""

"""Ejercicio 22 (Opcional)"""
"""
Sea G = <V, A> un grafo dirigido y ponderado con la función de costos C: A → R de forma tal que C(v, w) > 0 para todo arco <v, w> ∈ A. Se define el costo C(p) de todo camino 
p = <v0, v1, …, vk> como C(v0, v1) * C(v1, v2) * … * C(vk - 1, vk).
Demuestre que si p = <v0, v1, …, vk> es el camino de menor costo con respecto a C en ir de v0 hacia vk, entonces <vi, vi + 1, .., vj> es el camino de menor costo (también con respecto a C) en ir de vi a vj para todo 0 ≤ i < j ≤ k.
¿Bajo qué condición o condiciones se puede afirmar que con respecto a C existe camino de costo mínimo entre dos vértices  a, b∈V? Justifique su respuesta.
Demuestre que, usando la función de costos C tal y como la dan, no se puede aplicar el algoritmo de Dijkstra para hallar los costos de los caminos de costo mínimo desde un vértice de origen s hacia el resto.
Plantee un algoritmo, lo más eficiente en tiempo que usted pueda, que determine los costos de los caminos de costo mínimo desde un vértice de origen s hacia el resto usando la función de costos C.
Suponiendo que C(v, w) > 1 para todo <v, w>∈A, proponga una función de costos C’:A → R y además la forma de calcular el costo C’(p) de todo camino p = <v0, v1, …, vk> de forma tal que: aplicando el algoritmo de Dijkstra usando C’, se puedan obtener los costos (con respecto a la función original C) de los caminos de costo mínimo desde un vértice de origen s hacia el resto. Justifique su respuesta.
"""