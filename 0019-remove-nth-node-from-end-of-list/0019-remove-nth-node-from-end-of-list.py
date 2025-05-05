class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head) #0 value points to the head 
        left=dummy
        right=head

        #difference initial n
        while n>0 and right:
            right=right.next
            n-=1 
        while right:
            left=left.next
            right=right.next
        #delete
        left.next=left.next.next

        #not include dummy node in the return 
        return dummy.next 
        