# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # if not head.next:
        #     return head

        t=head
        p=head.next
        q=head.next.next
        head.next=None
        if not q:
            p.next=head
            return p
        while q:
            p.next=t
            t=p
            p=q
            q=q.next
        p.next=t   
        return p
        

        

