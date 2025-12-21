from typing import Any


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode'=None):
        self.val = val
        self.next = next
from typing import Optional

def parse_linked_list(ll: list) -> Optional[ListNode]:
    dummy = ListNode(val=0, next=None)
    head = dummy
    for el in ll:
        head.next = ListNode(val=el)
        head = head.next

    return dummy.next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=0, next=None)
        dummy.next = head
        one_step = dummy
        two_step = dummy

        while two_step.next != None and two_step.next.next != None:
            # if two_step.next != None and two_step.next.next == None:
                # return one_step.next
            # if two_step.next == None:
                # return one_step.next

            one_step = one_step.next
            two_step = two_step.next.next

        return one_step.next
    

list1 = parse_linked_list([1,2,3,4,5])
list2 = parse_linked_list([1,3,4])
c = Solution()
c.middleNode(list1)