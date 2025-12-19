# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head.next:
            return head
        if left == right:
            return head
        
        prev = None
        curr = head
        step = 0
        change = None
        dummy = head

        while curr:
            step += 1
            if step != left:
                head = head.next
                dummy = head
                continue
            if step == left:
                change = dummy
                while step != right - 1:
                   head = head.next
                   step += 1



            next_node = curr.next # first, make sure we don't lose the next node

            curr.next = prev      # reverse the direction of the pointer
            prev = curr           # set the current node to prev for the next node
            curr = next_node  

        return prev 

    
