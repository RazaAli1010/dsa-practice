# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        dummy=ListNode(1)
        dummy.next=head
        prev=dummy
        first=prev.next
        second=first.next
        while first and second:
            first.next=second.next
            second.next=first
            prev.next=second
            prev=first
            first=first.next
            if first:
                second=first.next
        return dummy.next

