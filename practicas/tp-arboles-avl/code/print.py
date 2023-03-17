" MUESTRA EN CONSOLA UNA LISTA"

def printLinkedlist(L):
  currentNode=L.head
  while currentNode!= None:
    if currentNode==L.head:
      print("[ ",end="")
      print(currentNode.value,", ", end="")
      currentNode=currentNode.nextNode
    else:
      if currentNode.nextNode!= None:
        print(currentNode.value,", ", end="")
        currentNode=currentNode.nextNode
      else:
        print(currentNode.value,"]", end="")
        currentNode=currentNode.nextNode
  print("")

" MUESTRA EN CONSOLA UN ARBOL BINARIO DE BUSQUEDA "

def printBinaryTree(Tree):
  PrintTreeR(Tree.root)
  print("")
def PrintTreeR(root):
    def height(root):
        return 1 + max(height(root.leftnode), height(root.rightnode)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.leftnode,level+1,x-seg,'l'))
            q.append((node.rightnode,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].value)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)  

" MUESTRA EN CONSOLA EL BF DE UN ARBOL BINARIO DE BUSQUEDA "

def printBinaryTreeBF(Tree):
  PrintTreeRBF(Tree.root)
  print("")
def PrintTreeRBF(root):
    def height(root):
        return 1 + max(height(root.leftnode), height(root.rightnode)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.leftnode,level+1,x-seg,'l'))
            q.append((node.rightnode,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].bf)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)  
def printBinaryTreeH(Tree):
  PrintTreeHR(Tree.root)
  print("")
  
def PrintTreeHR(root):
    def height(root):
        return 1 + max(height(root.leftnode), height(root.rightnode)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.leftnode,level+1,x-seg,'l'))
            q.append((node.rightnode,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].h)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)  