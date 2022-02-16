# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  
class BinaryTree(object):
  def __init__(self,root):
    self.root = Node(root)

  def print_tree(self, traversal_type):
    if traversal_type == "preorder":
      return self.preorder_print(self.root, "")
    else:
      print("Traversal type not supported")
      return False
  
  def preorder_print(self, start, traversal):
    if start != -1:
      traversal += (str(start.value) + "-")
      traversal = self.preorder_print(start.left, traversal)
      traversal = self.preorder_print(start.right, traversal)
    return traversal

def tree_creation(node_index, node, key, left, right):
    if node_index == -1:
        return
    else:
        node.left = key[left[node_index]]
        node.right = key[right[node_index]]
        tree_creation(left[node_index], node.left, key, left, right)
        tree_creation(right[node_index], node.right, key, left, right)


n = int(input())
key, left, right = [], [], []
for i in range(0, n):
    a, b, c = map(int, input().split())
    if i == 0:
        tree = BinaryTree(a)
    key.append(a)
    left.append(b)
    right.append(c)

tree_creation(0, tree.root, key, left, right)
    
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)
print(tree.print_tree("preorder"))