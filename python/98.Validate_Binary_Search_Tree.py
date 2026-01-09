# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        stack = [(root,-sys.maxsize,sys.maxsize)]

        while stack:

            node,minimum,maximum = stack.pop()
            print(f"pop: {node.val} {minimum} {maximum}")

            if node.val <= minimum or node.val >= maximum:
                print(f"exiting: {node.val} {minimum} {maximum}")
                return False
            
            if node.left is not None:
                stack.append((node.left,minimum,node.val))
            if node.right is not None:
                stack.append((node.right,node.val,maximum))

        return True
