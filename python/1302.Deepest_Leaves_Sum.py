# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return []

        result = []
        q = deque()
        q.appendleft(root)

        while q:

            num_nodes = len(q)
            level_sum = 0

            for i in range(num_nodes):
                node = q.pop()
    
                if node.left is not None:
                    q.appendleft(node.left)
                    
                if node.right is not None:
                    q.appendleft(node.right)
                    
                
                level_sum += node.val 
            
            result.append(level_sum)
        
        return result[-1]
    
