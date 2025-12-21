# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        q = deque()
        q.appendleft(root)

        while q:

            num_nodes = len(q)
            maximum = q[0].val

            for i in range(num_nodes): 

                node = q.pop()

                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right)
                
                maximum = max(maximum,node.val)
            
            result.append(maximum)
    
        return result
            

                
        