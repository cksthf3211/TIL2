import sys
sys.stdin = open('hello.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

# n, m = map(int, input().split())
# n = list(map(int, input().split()))

# 전위순회
def preorder(root):
    if root != '.':
        print(root, end='')       # root
        preorder(tree[root][0])   # left
        preorder(tree[root][1])   # right
 
# 중위순회 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])    # left
        print(root, end='')       # root
        inorder(tree[root][1])    # right
 
 
# 후위순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')       # root

tree = {}
for i in range(int(input())):
    root, left, right = input().strip().split()  
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')