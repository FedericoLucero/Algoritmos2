
############
class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None
############
  
############ add(L,element)
def add(L,element):
  nodox = Node()
  nodox.value = element
  nodox.nextNode = L.head
  L.head = nodox
############

############ search(L,element)
def search(L,element):
  cont = 0
  pos = None
  currentNode = L.head
  while currentNode != None:
    if currentNode.value == element:
      pos = cont
      currentNode = None
    else:
      currentNode = currentNode.nextNode
      cont += 1
  return pos
############
  
############ insert(L,element,position)
def insert(L,element,position):
  len = length(L)
  if len >= position:
    nodox = Node()
    nodox.value = element
    if len == 0:
      L.head=nodox
    else: 
      if position == 0:
        nodox.nextNode = L.head
        L.head = nodox
      else:
        cont = 0
        currentNode = L.head
        while currentNode != None :
          if cont == position-1:
            if currentNode.nextNode != None:
              nodox.nextNode = currentNode.nextNode
            currentNode.nextNode = nodox   
            currentNode = None
          else:
            currentNode=currentNode.nextNode
            cont += 1
  else:
    position = None
  return position
############

############ delete(L,element)
def delete(L,element):
  currentNode = L.head
  position = search(L,element)
  if position != None:
    if position != 0:
      currentNode = L.head
      cont = 0
      while currentNode != None and cont < position:
        if cont == position - 1:
          currentNode.nextNode = currentNode.nextNode.nextNode
        currentNode = currentNode.nextNode
        cont += 1
    else:
      L.head = currentNode.nextNode
  return position
############

############ length(L)
def length(L):
  currentNode = L.head
  len = 0
  while currentNode != None:
    len += 1
    currentNode = currentNode.nextNode
  return len
############

############ access(L,position)
def access(L,position):
  element = None
  cont = 0
  currentNode = L.head
  while currentNode != None and cont <= position:
    if cont == position:
      element = currentNode.value
    cont += 1
    currentNode = currentNode.nextNode
  return element
############

############ update(L,element,position)
def update(L,element,position):
  len = length(L)
  if len >= position:
    cont = 0
    currentNode = L.head
    while currentNode != None and cont <= position:
      if cont == position:
        currentNode.value = element
        position = cont
      cont += 1
      currentNode = currentNode.nextNode
  else:
    position = None
  return position
############
  

############ enqueue(Q,element)
def enqueue(Q,element):
  x=0
  currentNode=Q.head
  if currentNode==None:
    nodox=Node()
    nodox.value=element
    Q.head=nodox
  else:
    while currentNode!= None:
      if currentNode.nextNode == None and x==0:
        nodox=Node()
        nodox.value=element
        currentNode.nextNode=nodox
        x=1
      currentNode=currentNode.nextNode
############
      
############ dequeue(Q)
def dequeue(Q):
  
  currentNode=Q.head
  if currentNode==None:
    return None
  else:  
    num=currentNode.value
    Q.head=currentNode.nextNode
    return num
############