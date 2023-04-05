class Trie:
	root = None

class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False
  
""""Ejercicio 1"""
"""insert(T,element) 
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual  se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida"""

def insert(T,element):
  if search(T,element) == True:  ### Verifica si la palabra ya esta ingresada ###
    return False
  if T.root == None:  ### Si el arbol esta vacio ###
    NewNode = initialize_node("")
    T.root = NewNode
    
  TNode = T.root
  for ch in element:  ### Recorre cada letra del elemento (palabra) ###
    index = traverse_list(TNode.children,ch)
    if index == None:  ### No se encuetra la letra en la lista ###
      TNode = add_node(ch,TNode) ### Se agrega un nuevo nodo a la lista ###
    else:  ### Se encuentra la letra en la lista ###
      TNode = TNode.children[index]  ### Sigue al proximo nodo ###
  TNode.isEndOfWord = True
  return True
  
def initialize_node(ch):  ### Crea un nuevo nodo ###
  NewNode = TrieNode() 
  NewNode.children = []
  NewNode.key = ch
  return NewNode
  
def traverse_list(list,ch):  ### Recorre la lista ###
  for index, i in enumerate(list):
    if i.key == ch:
      return index
  return None
  
def add_node(ch,TNode):  ### Agrega un nodo a la lista ###
  NewNode = initialize_node(ch)
  TNode.children.append(NewNode)
  NewNode.parent = TNode 
  return NewNode

""""Ejercicio 2"""
"""search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
Salida: Devuelve False o True  según se encuentre el elemento."""

def search(T,element):
  if T.root == None:  ### Si el arbol esta vacio ###
    return False
    
  TNode = T.root
  for ch in element:  ### Recorre cada letra del elemento (palabra) ###
    index = traverse_list(TNode.children,ch) # O(n) #
    if index == None:  ### No se encuentra la letra en la lista ###
      return False
    else:  ### Se encuentra la letra en la lista ###
      TNode = TNode.children[index]  ### Sigue al proximo nodo ###
  if TNode.isEndOfWord == True:
    return True
  else: return False

""""Ejercicio 3"""
"""delete(T,element)
Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento."""

def delete(T,element):
  if search(T,element) == False:
    return False
    
  TNode = T.root
  for ch in element:  ### Recorre cada letra del elemento (palabra) ###
    index = traverse_list(TNode.children,ch)
    if index == None:  ### No se encuentra la letra en la lista ###
      return False
    else:  ### Se encuentra la letra en la lista ###
      TNode = TNode.children[index]  ### Sigue al proximo nodo ###
  if TNode.children != []:  ### Si la palabra a eliminar es parte de una palabra mas larga (hola,holanda) ###
    TNode.isEndOfWord == False
    return True
  else:
    delete_node(T,TNode)
    return True

def delete_node(T,TNode):  ### Elimina los nodos de forma recursiva ###
  temp = TNode 
  TNode = TNode.parent 
  TNode.children.remove(temp)  
  if TNode.isEndOfWord == True or TNode == T.root or len(TNode.children) > 0:  ### Casos donde parar de eliminar nodos ###
    return True
  else:
    delete_node(T,TNode)

"""Ejercicio 4"""
"""Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas las palabras del árbol que empiezan por p y sean de longitud n."""

def autocomplete_word_with_pattern(T,p,n):
  if T.root == None:  ### Si el arbol esta vacio ###
    return
    
  TNode = T.root
  for ch in p:
    index = traverse_list(TNode.children,ch)
    if index == None:  ### No se encuetra la letra en la lista ###
      return 
    else:  ### Se encuentra la letra en la lista ###
      TNode = TNode.children[index]  ### Sigue al proximo nodo ###
      
  p = p[:-1]  ### Elimina el ultimo caracter del patron ###
  res = []  ### Nueva lista para las palabras encontradas ###
  create_word_list(TNode,res,p,n)  ### Crea una lista con las palabras encontradas ###
  print(res)  ### Impreme la lista ###

def create_word_list(node,res,prefix,n):
  if node.isEndOfWord == True:  ### Fin de la palabra ###
    if n != None:  ### Si buscamos una palabra de una logitud concreta ###
      if len(prefix + node.key) == n: 
        res.append(prefix + node.key)  ### Agrega la palabra entera a la lista ###
    else:
      res.append(prefix + node.key)  ### Agrega la palabra entera a la lista ###
  for child in node.children:
    create_word_list(child,res,prefix + node.key,n) 

"""Ejercicio 5"""
"""Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario. Se considera que un  Trie pertenecen al mismo documento cuando:
-Ambos Trie sean iguales (esto se debe cumplir)
-Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.
En otras palabras, analizar si todas las palabras de T1 se encuentran en T2."""

""" Analizar el costo computacional """
""" create_word_list = O(n), equal = O(n) + O(n) """

def equal(T1,T2):
  res1 = [] 
  create_word_list(T1.root,res1,"",None)
  res2 = []
  create_word_list(T2.root,res2,"",None)
  if res1 == res2:  ### Compara ambas listas ###
    return True
  else:
    return False

"""Ejercicio 6"""
"""Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un carácter."""

def inverted_strings(T):
  res = []
  create_word_list(T.root,res,"",None)
  for word1 in res:  ### Recorre la lsita ###
    temp = word1
    word1 = word1[::-1]  ### Invierte la palabra ###
    for word2 in res:
      if word1 == word2: 
        print("(",temp,",",word2,")")
        return True  
  return False

"""Ejercicio 7"""
"""Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena “pal” devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. Por ejemplo, autoCompletar(T, ma’) devolvería “” si T presenta las cadenas “madera” y “mama”."""

def autoCompletar(T, cadena):
  if T.root == None:
    return False
    
  TNode = T.root
  for ch in cadena:
    index = traverse_list(TNode.children,ch)
    if index == None:  ### No se encuetra la letra en la lista ###
      return False
    else:  ### Se encuetra la letra en la lista ###
      TNode = TNode.children[index]  ### Sigue al proximo nodo ###

  TNode = TNode.children[index]
  res = []  ### Nueva lista para las palabras encontradas ###
  create_word_res_list(TNode,res,"") 
  print(res) ### Imprime la lista con todas las palabras encontradas ###
    
def create_word_res_list(node,res,prefix):
  if len(node.children) > 1 :  
    res.append(prefix + node.key)
  for child in node.children:
    create_word_res_list(child,res,prefix + node.key) 

"MUESTRA EN CONSOLA UNA LISTA DE LAS PALABRAS DEL TRIE"
def printTrie(T) :
  res = []
  create_word_list(T.root,res,"",None)  ### None para reutilizar la funcion en "patron" ###
  print(res)  ### Imprime la lista con todas las palabras encontradas ###