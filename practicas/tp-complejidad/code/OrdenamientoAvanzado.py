from linkedlist import *

def MergeSort(L):
  mergeSortR(L.head)
  return L
  
def mergeSortR(Node):
  if Node == None or Node.nextNode == None:
    return Node
  middle = getMiddle(Node)
  nextNodetomiddle = middle.nextNode

  middle.nextNode = None

  left = mergeSortR(Node)
  right = mergeSortR(nextNodetomiddle)

  sortedlist = sortedMerge(left, right)
  return sortedlist
	
def getMiddle(head):
  if head == None:
    return head

  Node_slow = head
  Node_fast = head

  while Node_fast.nextNode != None and Node_fast.nextNode.nextNode != None:
    Node_slow = Node_slow.nextNode
    Node_fast = Node_fast.nextNode.nextNode
    
  return Node_slow

def sortedMerge(left, right):
  result = None
  if left == None:
    return right
  if right == None:
    return left

  if left.value <= right.value:
    result = left
    result.nextNode = sortedMerge(left.nextNode, right)
  else:
    result = right
    result.nextNode = sortedMerge(left, right.nextNode)
  return result

################
def QuickSort(L):
  if L.head == None:
    return None
  definitiveList = LinkedList()
  definitiveList = QuickSortR(L, definitiveList)
  return definitiveList
  
def QuickSortR(L, definitiveList):
  list1 = LinkedList()
  list2 = LinkedList()
  len = length(L)
  if len > 1:
    if L.head.value > L.head.nextNode.value:
      pivot = L.head
    else:
      pivot = L.head.nextNode
    currentNode = L.head
    aux = L.head
    while currentNode != None:
      if currentNode.value >= pivot.value:
        L.head = L.head.nextNode
        enqueueNode(list2, currentNode)
      else:
        L.head = L.head.nextNode
        enqueueNode(list1, currentNode)
      currentNode = L.head

    QuickSortR(list1, definitiveList)
    QuickSortR(list2, definitiveList)
  elif L.head != None:
    enqueueNode(definitiveList, L.head)
  return definitiveList