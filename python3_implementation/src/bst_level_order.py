import sys

from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        ordered = []
        bst_queue = deque([])
        bst_queue.append(root)
        while(bst_queue):
            node = bst_queue.popleft()
            ordered.append(node.data)
            print(node.data, end=" ")
            if node.left is not None:
                bst_queue.append(node.left)
            if node.right is not None:
                bst_queue.append(node.right)

        return ordered

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
