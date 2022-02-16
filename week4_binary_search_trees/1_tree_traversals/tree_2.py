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
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inorder_print(self, start, result, key, left, right):
    if start != -1:
      result = self.inorder_print(left[start], result, key, left, right)
      result.append(key[start])
      result = self.inorder_print(right[start], result, key, left, right)
    return result

  def inOrder(self):
    self.result = []
    self.result = self.inorder_print(0, self.result, self.key, self.left, self.right)
    return self.result

  def preorder_print(self, start, result, key, left, right):
    if start != -1:
      result.append(key[start])
      result = self.preorder_print(left[start], result, key, left, right)
      result = self.preorder_print(right[start], result, key, left, right)
    return result

  def preOrder(self):
    self.result = []
    self.result = self.preorder_print(0, self.result, self.key, self.left, self.right)
    return self.result

  def postorder_print(self, start, result, key, left, right):
    if start != -1:
      result = self.postorder_print(left[start], result, key, left, right)
      result = self.postorder_print(right[start], result, key, left, right)
      result.append(key[start])
    return result

  def postOrder(self):
    self.result = []
    self.result = self.postorder_print(0, self.result, self.key, self.left, self.right)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()