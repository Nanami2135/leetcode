from typing import Optional

# Definition for singly-linked list.
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
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev
            


list1 = parse_linked_list([1,2,3,4,5])
# list2 = parse_linked_list([1,3,4])
c = Solution()
c.reverseList(list1)
        