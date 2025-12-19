# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        

class Solution:
    step = 1
    steps = []
    def minDepth(self, root: Optional[TreeNode]) -> int:
        print (root)

        if root.left == None and root.right == None:
            self.steps.append(self.step)
            self.step = self.step - 1
            return
        
        if root.left != None:
            self.step = self.step + 1
            self.minDepth(root.left)

        if root.right != None:
            self.step = self.step + 1
            self.minDepth(root.right)
        return (min(self.steps))
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        print (root)
        if root == None:
            return 0

        if root.left == None and root.right == None:
            
            return 1
        
        if root.left != None:
            left_depth = self.minDepth(root.left)
        else:
            left_depth = float('inf')

        if root.right != None:
            right_depth = self.minDepth(root.right)
        else:
            right_depth = float('inf')

        return min(left_depth, right_depth) + 1