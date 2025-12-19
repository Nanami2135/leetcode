from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        view = []
        q = deque()
        q.appendleft(root)

        while q:
            num_nodes = len(q)

            for i in range(num_nodes):
                node = q.pop()

                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

                # If node is rightmost one
                if i == num_nodes - 1:
                    view.append(node.val)

        return view

