# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def parse_linked_list(ll: list) -> Optional[ListNode]:
    dummy = ListNode(val=0, next=None)
    head = dummy
    for el in ll:
        head.next = ListNode(val=el)
        head = head.next

    return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=None)
        tail = dummy.next
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next

# dummy -> [1, 2, 4]
# ->
# head1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))



list1 = parse_linked_list([1,2,4])
list2 = parse_linked_list([1,3,4])
c = Solution()
c.mergeTwoLists(list1,list2)

