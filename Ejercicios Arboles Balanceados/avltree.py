from linkedlist import*

class AVLTree:
	root = None
  
class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None
  h = None

""" rotateLeft(Tree,avlnode)
Descripción: Implementa la operación rotación a la izquierda
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
Salida: retorna la nueva raíz """

def rotateLeft(Tree,avlnode): 
  sub_root = avlnode.parent 
  new_root = avlnode.rightnode
  left_son_nr = new_root.leftnode
  
  new_root.leftnode = avlnode
  avlnode.parent = new_root
  avlnode.rightnode = left_son_nr
  if left_son_nr != None: 
    left_son_nr.parent = avlnode
  new_root.parent = sub_root
  if new_root.parent == None: 
    Tree.root = new_root
  else:
    if new_root.parent.leftnode == avlnode:
      new_root.parent.leftnode = new_root
    else:
      new_root.parent.rightnode = new_root
  return new_root
  
""" rotateRight(Tree,avlnode)
Descripción: Implementa la operación rotación a la derecha 
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
Salida: retorna la nueva raíz """

def rotateRight(Tree,avlnode):
  sub_root = avlnode.parent 
  new_root = avlnode.leftnode
  right_son_nr = new_root.rightnode
  
  new_root.rightnode = avlnode
  avlnode.parent = new_root
  avlnode.leftnode = right_son_nr
  if right_son_nr != None: 
    right_son_nr.parent = avlnode
  new_root.parent = sub_root
  if new_root.parent == None:
      Tree.root = new_root
  else:
    if new_root.parent.leftnode == avlnode:
      new_root.parent.leftnode = new_root
    else:
      new_root.parent.rightnode = new_root
  return new_root
  
""" calculateBalance(AVLTree) 
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
Entrada: El árbol AVL  sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol """

def calculateBalance(AVLTree):
  calculateBalanceR(AVLTree.root)
  
def calculateBalanceR(avlnode):
  if avlnode == None:
    return
  
  avlnode.bf = calculate_height(avlnode.leftnode) - calculate_height(avlnode.rightnode)
  calculateBalanceR(avlnode.leftnode)
  calculateBalanceR(avlnode.rightnode)
    
def calculate_height(avlnode):
  if avlnode == None:
    return 0
  avlnode.h = max(calculate_height(avlnode.leftnode),calculate_height(avlnode.rightnode)) + 1
  return avlnode.h

"""" reBalance(AVLTree)
Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
Entrada: El árbol binario de tipo AVL sobre el cual se quiere operar.
Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad."""

def reBalance(AVLTree):
  calculateBalance(AVLTree)
  reBalanceR(AVLTree,AVLTree.root)

def reBalanceR(AVLTree,avlnode):
  if avlnode == None:
    return
  reBalanceR(AVLTree,avlnode.leftnode)
  if abs(avlnode.bf) >= 2:
    if avlnode.bf < 0:
      if avlnode.rightnode.bf > 0:
        rotateRight(AVLTree,avlnode.rightnode)
        rotateLeft(AVLTree,avlnode)
      else:
        rotateLeft(AVLTree,avlnode)
      calculateBalanceR(avlnode)
    elif avlnode.bf > 0:
      if avlnode.leftnode.bf < 0:
       rotateLeft(AVLTree,avlnode.leftnode)
       rotateRight(AVLTree,avlnode)
      else:
       rotateRight(AVLTree,avlnode)
    update_bf(AVLTree,avlnode)
  reBalanceR(AVLTree,avlnode.rightnode)

""" OPERACIONES REIMPLEMENTADAS """

""" INSERT AVL """

def insert(B,element,key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key
  newNode.h = 0
  newNode.bf = 0
  if B.root == None:
    B.root = newNode
    return B
  else:
    avlnode = insertAVLR(newNode, B.root)
    if avlnode != None:
      update_bf(B,avlnode.parent)
  return B
  
def insertAVLR(newNode, avlnode):
  if newNode.key > avlnode.key:
    if avlnode.rightnode == None:
      newNode.parent = avlnode
      avlnode.rightnode = newNode
      return newNode
    else:
      return insertAVLR(newNode, avlnode.rightnode)
  elif newNode.key < avlnode.key:
    if avlnode.leftnode == None:
      newNode.parent = avlnode
      avlnode.leftnode = newNode
      return newNode
    else:
      return insertAVLR(newNode, avlnode.leftnode)
  elif newNode.key == avlnode.key:
    return None

def update_bf(B,avlnode):
  if avlnode != None:
    if (avlnode.rightnode != None) and (avlnode.leftnode == None):
      avlnode.h += 1
      avlnode.bf = avlnode.h
    elif (avlnode.leftnode != None) and (avlnode.rightnode == None):
      avlnode.h += 1
      avlnode.bf = -avlnode.h
    elif (avlnode.rightnode != None) and (avlnode.leftnode != None):
      avlnode.h = max(avlnode.rightnode.h, avlnode.leftnode.h) + 1
      avlnode.bf = avlnode.leftnode.h - avlnode.rightnode.h
    elif (avlnode.rightnode == None) and (avlnode.leftnode == None):
      avlnode.h = 0
      avlnode.bf = 0
    if (avlnode.bf < -1) or (avlnode.bf > 1):
      reBalance(B)
    update_bf(B,avlnode.parent)
  else:
    return B

""" DELETE AVL """

def delete(B,element):
  key = search(B,element)
  if key != None:
    node = deleteAVL(B.root,key,B)
    calculateBalance(B)
  
def deleteAVL(avlnode, key, B):
  if avlnode == None:
    return
  if key < avlnode.key:
    avlnode.leftnode = deleteAVL(avlnode.leftnode, key, B)
  elif key > avlnode.key:
    avlnode.rightnode = deleteAVL(avlnode.rightnode, key, B)
  else:
    if avlnode.leftnode == None:
      temp = avlnode.rightnode
      root = None
      return temp
    elif avlnode.rightnode == None:
      temp = avlnode.leftnode
      root = None
      return temp
    temp = menor_de_los_mayores(root.rightnode)
    avlnode.key = temp.key
    avlnode.rightnode = deleteAVL(avlnode.rightnode,temp.key,B)
  if avlnode == None:
    return avlnode
    
  avlnode.h = max(calculate_height(avlnode.leftnode),calculate_height(avlnode.rightnode)) + 1
  balance = get_node_balance(avlnode)
  
  if (balance > 1):
    if (get_node_balance(avlnode.leftnode) < 0):
      avlnode.leftnode = get_node_balance(B,avlnode.leftnode)
    return rotateRight(B,avlnode)
    
  if (balance < -1): 
    if (get_node_balance(avlnode.rightnode) > 0):
      avlnode.rightnode = get_node_balance(avlnode.rightnode)
    return rotateLeft(B,avlnode)
  return avlnode
 
def get_node_balance(avlnode):
  if avlnode == None:
    return 0
  return calculate_height(avlnode.leftnode) - calculate_height(avlnode.rightnode)
  
" BINARYTRE FUNCIONES ADAPTADAS A AVLTREE "

"search(B,element)"
"Descripción: Busca un elemento en el TAD árbol binario."
"Entrada: el árbol binario B en el cual se quiere realizar la búsqueda (BinaryTree) y el valor del elemento (element) a buscar."
"Salida: Devuelve la key asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra."

def search(B,element):
  return searchR(B.root,element)
  
def searchR(currentNode,element):
  if currentNode == None:
    return
  else:
    if currentNode.value == element:
      return currentNode.key
    else:
      if searchR(currentNode.leftnode,element) != None:
        return searchR(currentNode.leftnode,element)
      if searchR(currentNode.rightnode,element) != None:
        return searchR(currentNode.rightnode,element)

"insert(B,element,key)"
"Descripción: Inserta un elemento con una clave determinada del TAD árbol binario."
"Entrada: el árbol B sobre el cual se quiere realizar la inserción (BinaryTree), el valor del elemento (element) a insertar y la clave (key) con la que se lo quiere insertar."
"Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None."

def insertBT(B,element,key):
  newNode = AVLNode()
  newNode.key = key
  newNode.value = element
  insertBTR(newNode,B.root,B)
  
def insertBTR(newNode,currentNode,B):
  if currentNode != None:
    if currentNode.key != newNode.key:
      if newNode.key > currentNode.key:
        if currentNode.rightnode == None:
          currentNode.rightnode = newNode
          newNode.parent=currentNode
          return currentNode.key
        else:
          insertBTR(newNode,currentNode.rightnode,B)
      else:
        if currentNode.leftnode == None:
          currentNode.leftnode = newNode
          newNode.parent = currentNode
          return currentNode.key
        else:
          insertBTR(newNode,currentNode.leftnode,B)
    else:
      return None
  else:
    B.root = newNode
    return newNode.key
    
"delete(B,element)"
"Descripción: Elimina un elemento del TAD árbol binario"
"Poscondición: Se debe desvincular el Node a eliminar."
"Entrada: el árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor del elemento (element) a eliminar."
"Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra."

def deleteBT(B,element):
  key = search(B,element)
  if key != None:
    return deleteBTR(B.root,key,B)
  
"deleteKey(B,key)"
"Descripción: Elimina una clave del TAD árbol binario."
"Poscondición: Se debe desvincular el Node a eliminar."
"Entrada: el árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor de la clave (key) a eliminar."
"Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento a eliminar no se encuentra."

def deleteKeyBT(B,key):
  return deleteBTR(B.root,key,B)

"DELETE Y DELETEKEY AUX"

def menor_de_los_mayores(currentNode):
  currentNode = currentNode.rightnode
  while currentNode.leftnode != None:
    currentNode = currentNode.leftnode
  return currentNode
      
def mayor_de_los_menores(currentNode):
  currentNode = currentNode.leftnode
  while currentNode.rightnode != None: 
    currentNode = currentNode.rightnode
  return currentNode

def deleteBTR(currentNode, key,B):
  if currentNode == None:
    return None
  else:
    if key > currentNode.key:
      currentNode = currentNode.rightnode
      return deleteBTR(currentNode,key,B)
      
    elif key < currentNode.key:
      currentNode = currentNode.leftnode
      return deleteBTR(currentNode,key,B)
      
    else: 
      if currentNode == B.root: #Raiz
        node_delete = currentNode
        if currentNode.leftnode != None and currentNode.rightnode == None:
          currentNode = mayor_de_los_menores(currentNode)
        else:
          currentNode = menor_de_los_mayores(currentNode)

        if currentNode.parent.rightnode == currentNode:
          currentNode.parent.rightnode = None
        else:
          currentNode.parent.leftnode = None

        if node_delete.leftnode != None:
          if node_delete.leftnode.parent == node_delete:
            node_delete.leftnode.parent = currentNode
        if node_delete.rightnode != None:
          if node_delete.rightnode.parent == node_delete:
            node_delete.rightnode.parent = currentNode
          
        currentNode.leftnode = node_delete.leftnode
        currentNode.rightnode = node_delete.rightnode
        currentNode.parent = None
        node_delete = None

        B.root = currentNode
        
      else: #Hoja
        if currentNode.leftnode == None and currentNode.rightnode == None: 
          if currentNode.parent.leftnode == currentNode:
            currentNode.parent.leftnode = None
          else:
            currentNode.parent.rightnode = None
            
        else: #Rama
          node_delete = currentNode
          if currentNode.leftnode != None and currentNode.rightnode == None:
            currentNode = mayor_de_los_menores(currentNode)
          else:
            currentNode = menor_de_los_mayores(currentNode)

          if currentNode.parent.rightnode == currentNode:
            currentNode.parent.rightnode = None
            
          if node_delete.parent.leftnode == node_delete:
            node_delete.parent.leftnode = currentNode
            
          if currentNode.parent.leftnode == currentNode:
            currentNode.parent.leftnode = None
            
          if node_delete.parent.rightnode == node_delete:
            node_delete.parent.rightnode=currentNode

          currentNode.leftnode = node_delete.leftnode
          currentNode.rightnode = node_delete.rightnode
          currentNode.parent = node_delete.parent
          node_delete = None
          
      return key
      
"access(B,key)"
"Descripción: Permite acceder a un elemento del árbol binario con una clave determinada."
"Entrada: El árbol binario (BinaryTree) y la key del elemento al cual se quiere acceder."
"Salida: Devuelve el valor de un elemento con una key del árbol binario, devuelve None si no existe elemento con dicha clave."

def access(B,key):
  return accessR(key,B.root)
  
def accessR(key,currentNode):
  if currentNode == None:
    return None
  else:
    if key > currentNode.key:
      currentNode = currentNode.rightnode
      return accessR(key,currentNode)
    elif key < currentNode.key:
      currentNode = currentNode.leftnode
      return accessR(key,currentNode)
    else:
      return currentNode.value
    
"update(L,element,key)"
"Descripción: Permite cambiar el valor de un elemento del árbol binario con una clave determinada."
"Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual se quiere asignar el valor de element."
"Salida: Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update."

def update(B,element,key):
  return updateR(B.root,element,key)

def updateR(currentNode,element,key):
  if currentNode == None:
    return None
  else:
    if key > currentNode.key:
      currentNode = currentNode.rightnode
      return updateR(currentNode,element,key)
    elif key < currentNode.key:
      currentNode = currentNode.leftnode
      return updateR(currentNode,element,key)
    else:
      currentNode.value = element
      return currentNode.key
      
"traverseInOrder(B)"
"Descripción: Recorre un árbol binario en orden"
"Entrada: El árbol binario (BinaryTree)"
"Salida: Devuelve una lista (LinkedList) con los elementos del árbol en orden. Devuelve None si el árbol está vacío."

def traverseInOrder(B):
  L = LinkedList()
  inorder(B.root,L)
  return L
  
def inorder(currentNode,L):
  if currentNode == None:
    return
  inorder(currentNode.leftnode,L)
  enqueue(L,currentNode.value)
  inorder(currentNode.rightnode,L)
  
"traverseInPostOrder(B)"
"Descripción: Recorre un árbol binario en post-orden"
"Entrada: El árbol binario (BinaryTree)"
"Salida: Devuelve una lista (LinkedList) con los elementos del árbol en post-orden. Devuelve None si el árbol está vacío."
  
def traverseInPostOrder(B):
  L=LinkedList()
  posorder(B.root,L)
  return L
  
def posorder(currentNode,L):
  if currentNode == None:
    return
  posorder(currentNode.leftnode,L)
  posorder(currentNode.rightnode,L)
  enqueue(L,currentNode.value)
 
"traverseInPreOrder(B)"
"Descripción: Recorre un árbol binario en pre-orden"
"Entrada: El árbol binario (BinaryTree)"
"Salida: Devuelve una lista (LinkedList) con los elementos del árbol en pre-orden. Devuelve None si el árbol está vacío."
  
def traverseInPreOrder(B):
  L=LinkedList()
  presorder(B.root,L)
  return L
  
def presorder(currentNode,L):
  if currentNode == None:
    return
  enqueue(L,currentNode.value)
  presorder(currentNode.leftnode,L)
  presorder(currentNode.rightnode,L)

"traverseInPreOrder(B)"
"Descripción: Recorre un árbol binario en pre-orden"
"Entrada: El árbol binario (BinaryTree)"
"Salida: Devuelve una lista (LinkedList) con los elementos del árbol en pre-orden. Devuelve None si el árbol está vacío."

def traverseBreadFirst(B):
  L = LinkedList() 
  currentNode = B.root
  h = height(currentNode) 
  for i in range(1, h+1): 
    CurrentLevel(currentNode,i,L)
  return L
 
def CurrentLevel(currentNode, level,L):
  if currentNode == None:
    return
  if level == 1:
    enqueue(L,currentNode.value)
  elif level > 1:
    CurrentLevel(currentNode.leftnode, level-1,L)
    CurrentLevel(currentNode.rightnode, level-1,L)
 
def height(node): 
  if node == None:
    return 0
  else:
    leftheight = height(node.leftnode)
    righheight = height(node.rightnode)

    if leftheight > righheight: 
      return leftheight+1
    else:
      return righheight+1