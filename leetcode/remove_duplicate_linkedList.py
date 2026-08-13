
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        i=head
        while i and i.next:
            if i.val==i.next.val:
                i.next=i.next.next
            else:
                i=i.next
        return head

        