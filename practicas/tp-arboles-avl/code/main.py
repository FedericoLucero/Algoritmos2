from avltree import*
from print import*

print(" //////////// EJERCICIO 1 //////////// ")

A = AVLTree()
insertBT(A, 40, 40)
insertBT(A, 50, 50)
insertBT(A, 60, 60)

print(" DESBALANCEADO ")
printBinaryTree(A)

rotateLeft(A,A.root)

print(" BALANCEADO - ROTACION HACIA LA IZQUIERZA ")
printBinaryTree(A)

B = AVLTree()
insertBT(B, 60, 60)
insertBT(B, 50, 50)
insertBT(B, 40, 40)

print(" DESBALANCEADO ")
printBinaryTree(B)

rotateRight(B,B.root)

print(" BALANCEADO - ROTACION HACIA LA DERECHA ")
printBinaryTree(B)

C = AVLTree()
insertBT(C, 50, 50)
insertBT(C, 60, 60)
insertBT(C, 40, 40)
insertBT(C, 45, 45)
insertBT(C, 30, 30)
insertBT(C, 70, 70)
insertBT(C, 65, 65)
insertBT(C, 75, 75)

print(" DESBALANCEADO ")
printBinaryTree(C)

rotateLeft(C,C.root.rightnode)

print(" BALANCEADO - ROTACION HACIA LA IZQUIERZA ")
printBinaryTree(C)

print("")

print(" //////////// EJERCICIO 2 //////////// ")
print("")

calculateBalance(C)

print(" BALANCEADO - CALCULATE BALANCE FACTOR ")
printBinaryTree(C)

print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(C)

print("")

print(" //////////// EJERCICIO 3 //////////// ")

D = AVLTree()
insertBT(D, 50, 50)
insertBT(D, 60, 60)
insertBT(D, 40, 40)
insertBT(D, 45, 45)
insertBT(D, 30, 30)
insertBT(D, 70, 70)
insertBT(D, 65, 65)
insertBT(D, 75, 75)

print(" DESBALANCEADO ")
printBinaryTree(D)
calculateBalance(D)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(D)

reBalance(D)
print(" BALANCEADO - RE BALANCE")
printBinaryTree(D)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(D)

E = AVLTree()
insertBT(E, 50, 50)
insertBT(E, 60, 60)
insertBT(E, 70, 70)
insertBT(E, 65, 65)

calculateBalance(E)

print(" DESBALANCEADO ")
printBinaryTree(E)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(E)

reBalance(E)
print(" BALANCEADO - RE BALANCE")
printBinaryTree(E)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(E)

F = AVLTree()
insertBT(F, 50, 50)
insertBT(F, 60, 60)
insertBT(F, 40, 40)
insertBT(F, 45, 45)
insertBT(F, 30, 30)
insertBT(F, 70, 70)
insertBT(F, 65, 65)

calculateBalance(F)

print(" DESBALANCEADO ")
printBinaryTree(F)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(F)

reBalance(F)

print(" DESBALANCEADO ")
printBinaryTree(F)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(F)

print(" //////////// EJERCICIO 4 //////////// ")
"insertAVL"

G = AVLTree()
insert(G,50,50)
insert(G,40,40)
insert(G,60,60)
insert(G,70,70)
insert(G,20,20)
insert(G,45,45)
insert(G,55,55)
insert(G,80,80)
insert(G,90,90)
insert(G,100,100)

print(" BALANCEADO - INSERT AVL ")
printBinaryTree(G)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(G)
print(" PRINT H ")
printBinaryTreeH(G)

print(" //////////// EJERCICIO 5 //////////// ")
"deleteAVL"

H = AVLTree()
insert(H,50,50)
insert(H,40,40)
insert(H,60,60)
insert(H,70,70)
insert(H,20,20)
insert(H,45,45)
insert(H,55,55)
insert(H,80,80)
insert(H,90,90)
insert(H,100,100)
insert(H,200,200)

print(" BALANCEADO - INSERT AVL ")
printBinaryTree(H)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(H)
print(" PRINT H ")
printBinaryTreeH(H)

print(" BALANCEADO - DELETE AVL ")
delete(H,80)

printBinaryTree(H)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(H)
print(" PRINT H ")
printBinaryTreeH(H)

print(" BALANCEADO - DELETE AVL ")
delete(H,70)

printBinaryTree(H)
print(" PRINT BALANCE FACTOR ")
printBinaryTreeBF(H)
print(" PRINT H ")
printBinaryTreeH(H)