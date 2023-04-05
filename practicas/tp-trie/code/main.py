from trie import*
"Parte 1"
print("""Ejercicio 1""")
print("""insert""")
T1 = Trie()
lista = ["HOLA","HI","PAPA","HOLA","PATATA"]
for word in lista:
  if insert(T1,word) == True:
    print("SE INSERTO LA PALABRA (",word,")")
  else:
    print("LA PALABRA (",word,") YA ESTA EN EL TRIE")
print("")

print(""""Ejercicio 2""")
print("""search""")
lista = ["HOLA","HI","PAPA","PATAGONIA"]
for word in lista:
  if search(T1,word) == True:
    print("SE ENCONTRO LA PALABRA (",word,")")
  else:
    print("NO SE ENCONTRO LA PALABRA (",word,")")
print("")
print("""printTrie""")
printTrie(T1)
print("")

print("""Ejercicio 3""")
print("""delete""")
lista = ["HOLA"]
for word in lista:
  if delete(T1,word) == True:
    print("SE ELIMINO LA PALABRA (",word,")")
  else:
    print("NO SE ENCONTRO LA PALABRA (",word,")")
printTrie(T1)

"Parte 2"
print("")
print("""Ejercicio 4""")
"""Implementar un algoritmo que dado un árbol Trie T, un patrón p y un entero n, escriba todas las palabras del árbol que empiezan por p y sean de longitud n."""
    
autocomplete_word_with_pattern(T1,"PA",4)

print("")
print("""Ejercicio 5""")
"""Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario. Se considera que un  Trie pertenecen al mismo documento cuando:
-Ambos Trie sean iguales (esto se debe cumplir)
-Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.
En otras palabras, analizar si todas las palabras de T1 se encuentran en T2."""

T2 = Trie()
lista = ["HI","PAPA","PATATA"]
for word in lista:
  insert(T2,word)
if equal(T1,T2) == True:
  print("PERTENECEN AL MISMO DOCUMENTO")
else:
  print("NO PERTENECEN AL MISMO DOCUMENTO")

print("")
print("""Ejercicio 6""")
"""Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un carácter."""

insert(T1,"HOLA")
insert(T1,"ALOH")
printTrie(T1)
if inverted_strings(T1) == True:
  print("SE ENCUENTRO UNA CADENA INVERTIDA")
else:
  print("NO SE ENCUENTRO UNA CADENA INVERTIDA")

print("")
print("""Ejercicio 7""")
"""Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena “pal” devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. Por ejemplo, autoCompletar(T, ma’) devolvería “” si T presenta las cadenas “madera” y “mama”."""

T3 = Trie()
lista3 = ["GROENLANDIA","GROENLANDES"]
for word in lista3:
  if insert(T3,word) == True:
    print("SE INSERTO LA PALABRA (",word,")")
  else:
    print("LA PALABRA (",word,") YA ESTA EN EL TRIE")
print("")

autoCompletar(T3,"GROEN")