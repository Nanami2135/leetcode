# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if root is None:
            return 0

        min_dif = float('inf')
        stack = [root]
        result = 1000000000

        while stack:

            node = stack.pop()
            value = abs(node.val - target)

            print(f"result: {min_dif}")
            print (f"node.val: {node.val}")
            print (f"abs_value: {abs(value)}")
            
            if value <= min_dif:
                min_dif = value
                if result > node.val:
                    result = node.val

            print("-----")
            print(f"result_node: {result}")
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        
        return result
