# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.parent = [-1 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
      if b != -1:
        self.parent[b] = i
      if c != -1:
        self.parent[c] = i
    # print(self.key)
    # print(self.parent)

  def izquierda(self, i, algoritmo):
    # print(f"El nodo en el que estoy es {i}, el de su izquierda {self.left[i]}")
    if algoritmo == "preOrder" and self.left[i] != -1:
        self.result.append(self.key[i])
    if self.left[i] != -1:
      i = self.left[i] # Bajo a la izquierda
      self.look_left = True
      self.look_right = True
      self.not_print = False
    else:
    #   print("Look left es False")
      self.look_left = False
      self.not_print = False
    return i

  def derecha(self, i, algoritmo):
    if algoritmo == "preOrder":
        if self.not_print == False:
            self.result.append(self.key[i])
    elif algoritmo == "inOrder":
        self.result.append(self.key[i])
    # print(self.key[i])
    self.look_right = False
    if self.right[i] != -1:
        i = self.right[i]
        self.look_right = True
        self.look_left = True
        self.not_print = False
    else:
        self.look_left = False
        self.look_right = False
        self.not_print = False
    return i
  
  def desde_hijo_izq(self, i):
    if self.parent[i] != -1:
        i = self.parent[i]
    self.look_left = False
    self.look_right = True
    self.not_print = True
    return i
    
  def desde_hijo_der(self, i):
    if self.parent[i] != -1:
        i = self.parent[i]
    self.look_left = False
    self.look_right = False
    self.not_print = False
    return i

  def inOrder(self):
    self.result = []

    i = self.parent.index(-1) # Se empieza por el nodo raiz
    self.look_left = True
    self.look_right = True
    while len(self.result) < len(self.key):
      # Izquierda
      if self.left[i] != -1 and self.look_left:
        # print("Entra en izquierda")
        i = self.izquierda(i, "inOrder")
        continue

      # Derecha
      if self.look_right:
        # print("Entra en derecha")
        i = self.derecha(i, "inOrder")
        continue

      # Comprobacion derecha o izquierda
      child = "left"
      
      try:
        # Quiero saber si i está en la lista de hijos izquierdos
        self.left.index(i)
      except:
        child = "right"

      # Si izquierda
      if child == "left":
        i = self.desde_hijo_izq(i)
      
      # Si derecha
      elif child == "right":
        i = self.desde_hijo_der(i)

    return self.result

  def preOrder(self):
    self.result = []
    
    i = self.parent.index(-1) # Se empieza por el nodo raiz
    self.look_left = True
    self.look_right = True
    self.not_print = False
    while len(self.result) < len(self.key):
      # Izquierda
      if self.left[i] != -1 and self.look_left:
        # print("Entra en izquierda")
        i = self.izquierda(i, "preOrder")
        continue

      # Derecha
      if self.look_right:
        # print("Entra en derecha")
        i = self.derecha(i, "preOrder")
        continue

      # Comprobacion derecha o izquierda
      child = "left"
      
      try:
        # Quiero saber si i está en la lista de hijos izquierdos
        self.left.index(i)
      except:
        child = "right"

      # Si izquierda
      if child == "left":
        i = self.desde_hijo_izq(i)
      
      # Si derecha
      elif child == "right":
        i = self.desde_hijo_der(i)
    
    return self.result

  def postOrder(self):
    self.result = []
    
    i = self.parent.index(-1) # Se empieza por el nodo raiz
    self.look_left = True
    self.look_right = True
    self.not_print = False
    while len(self.result) < len(self.key):
      # Izquierda
      if self.left[i] != -1 and self.look_left:
        # print("Entra en izquierda")
        i = self.izquierda(i, "postOrder")
        continue

      # Derecha
      if self.look_right:
        # print("Entra en derecha")
        i = self.derecha(i, "postOrder")
        continue

      if self.right[i] == -1 and self.left[i] == -1:
        self.result.append(self.key[i])

      # Comprobacion derecha o izquierda
      child = "left"
      
      try:
        # Quiero saber si i está en la lista de hijos izquierdos
        self.left.index(i)
      except:
        child = "right"

      # Si izquierda
      if child == "left":
        i = self.desde_hijo_izq(i)
        if self.right[i] == -1:
            self.result.append(self.key[i])
      
      # Si derecha
      elif child == "right":
        i = self.desde_hijo_der(i)
        self.result.append(self.key[i])

    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()