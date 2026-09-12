# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        n, tail=1, head
        while tail.next:
            tail=tail.next
            n+=1
        k=k%n
        if k==0:
            return head
        tail.next=head
        steps_to_new_tail=n-k-1
        newTail=head
        for _ in range(steps_to_new_tail):
            newTail=newTail.next
        newHead=newTail.next
        newTail.next=None
        return newHead
        