"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        a=head
        if a==None:
            return a
        if a.next==None:
            if a.random:
                copy=Node(a.val,None,None)
                copy.random=copy
                return copy
            else:
                return Node(a.val,None,None)
        while a!=None:
            copy= Node(a.val,a.next,None)
            a.next=copy
            a=a.next.next

        a=head
        while a!=None:
            if a.next and a.random :
                a.next.random=a.random.next
            a=a.next.next
        a=head.next
        while a.next!=None:
            a.next=a.next.next
            a=a.next
        a=head.next
        return a


