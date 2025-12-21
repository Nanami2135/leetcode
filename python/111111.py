from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


number1 = [2,4,3]
number2 = [5,6,4]

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
    
