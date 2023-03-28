from OrdenamientoAvanzado import*

""" Ejercicio 4: Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del medio de la lista contiene antes que él en la lista la mitad de los elementos menores que él. Explique la estrategia de ordenación utilizada. """

def MergeList(L):
  L = MergeSort(L)
  last_node = L.head
  while last_node.nextNode != None:
    last_node = last_node.nextNode
  medio1 = getMiddle(L.head,last_node)
  medio2 = getMiddle(L.head,medio1)
  medio3 = getMiddle(medio1.nextNode,last_node)

  temp0 = L.head
  temp1 = medio2.nextNode
  temp2 = medio1.nextNode
  temp3 = medio3.nextNode

  L.head = temp2
  medio3.nextNode = temp1
  medio1.nextNode = temp0
  medio2.nextNode = temp3

  return L
def getMiddle(head,last_node):
  if head == None:
    return head
  Node_slow = head
  Node_fast = head
  while ((Node_fast.nextNode != last_node.nextNode) and (Node_fast.nextNode.nextNode != last_node.nextNode)):
    Node_slow = Node_slow.nextNode
    Node_fast = Node_fast.nextNode.nextNode
  return Node_slow

""" Ejercicio 5: Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un entero n y devuelve True si existen en A un par de elementos que sumados den n. Analice el costo computacional. """

def  ContieneSuma(A,n):
  node1 = A.head
  node2 = A.head

  while node1.nextNode != None:
    while node2.nextNode != None:
      if node1.value + node2.value == n:
        return True
      node2 = node2.nextNode
    node1 = node1.nextNode
  return False