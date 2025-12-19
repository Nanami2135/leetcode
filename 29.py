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


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        number1 = []
        number2 = []

        while l1:
            number1.append(l1.val)
            l1 = l1.next
        
        while l2:
            number2.append(l2.val)
            l2 = l2.next

        string1 = ""
        string2 = ""

        for i in range(len(number1)-1,-1,-1):
            string1 += str(number1[i])
        
        for i in range(len(number2)-1,-1,-1):
            string2 += str(number2[i])
        
        summa = int(string1) + int(string2)

        summa = str(summa)

        dummy = ListNode(val=0,next=None)
        tail = dummy

        for i in reversed(summa):
            tail.next = ListNode(val=i)
            tail = tail.next

            
        return dummy.next



list1 = parse_linked_list([2,4,3])
list2 = parse_linked_list([5,6,4])
c = Solution()
c.addTwoNumbers(list1,list2)


