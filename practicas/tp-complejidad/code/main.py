from linkedlist import*
from ejercicios import*
from print import*

L1 = LinkedList()
add(L1,10)
add(L1,9)
add(L1,8)
add(L1,7)
add(L1,6)
add(L1,5)
add(L1,4)
add(L1,3)
add(L1,2)
add(L1,1)
add(L1,0)

printLinkedlist(L1)
MergeList(L1)
printLinkedlist(L1)

L2 = LinkedList()
add(L2,5)
add(L2,4)
add(L2,3)
add(L2,2)
add(L2,1)
add(L2,0)
printLinkedlist(L2)
print(ContieneSuma(L2,1))
