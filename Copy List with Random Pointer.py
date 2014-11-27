# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        p=head
        while p is not None:
            p1=p.next
            p.next=RandomListNode(p.label)
            p.next.next=p1
            p=p1

        p=head
        while p is not None:
            if p.random is not None:
                p.next.random=p.random.next
            p=p.next.next

        p=head
        p2=p.next
        p3=None
        while p is not None:
            if p3 is None:
                p3=p.next
            else:
                p3.next=p.next
                p3=p3.next
            p.next=p.next.next
            p=p.next

        return p2
        
