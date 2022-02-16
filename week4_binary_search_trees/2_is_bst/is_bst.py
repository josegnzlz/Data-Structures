#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size

def inorder_print(start, result, key, left, right):
  if start != -1:
    result = inorder_print(left[start], result, key, left, right)
    result.append(key[start])
    # print(result)
    result = inorder_print(right[start], result, key, left, right)
  return result

def inOrder(key, left, right):
  result = []
  result = inorder_print(0, result, key, left, right)
  return result

def IsBinarySearchTree(key, left, right):
  # Implement correct algorithm here
  result = inOrder(key, left, right)
  # print(result)
  for i in range(0,len(result)-1):
    if result[i] >= result[i+1]:
      return False
  return True


def main():
  nodes = int(input())
  key, left, right = [], [], []
  for i in range(nodes):
    a,b,c = map(int, input().split())
    key.append(a)
    left.append(b)
    right.append(c)
  # print(key, left, right)
  if nodes == 0:
    print("CORRECT")
  elif IsBinarySearchTree(key, left, right):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
