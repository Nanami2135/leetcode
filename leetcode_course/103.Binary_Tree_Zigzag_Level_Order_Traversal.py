# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        level = 0
        q = deque([root])

        while q:
            node_level = len(q)
            numbers = []

            level_nodes = []
            for i in range(node_level):
                level_nodes.append(q.popleft())

            for node in level_nodes:
                numbers.append(node.val)
                if level%2 != 0:
                    if node.right is not None:
                        q.appendleft(node.right)
                    if node.left is not None:
                        q.appendleft(node.left)
                if level%2 == 0:
                    if node.left is not None:
                        q.appendleft(node.left)
                    if node.right is not None:
                        q.appendleft(node.right)

            level += 1
            result.append(numbers)
        
        return result