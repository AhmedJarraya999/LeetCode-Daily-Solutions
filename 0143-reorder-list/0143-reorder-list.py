class Solution(object):
    def reorderList(self, head):
        #2pointers
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # enos ethni taa linked list
        second=slow.next
        slow.next=None
        prev=None

        #reverse second portion of the linked list
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp

        #merge the two portions
        first=head
        second=prev
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2

        
        