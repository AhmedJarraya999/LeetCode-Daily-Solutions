# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy=ListNode(0,head)
        prev,cur=dummy,head
        while cur and cur.next:
            nxtPair=cur.next.next
            second=cur.next

            second.next=cur
            cur.next=nxtPair
            prev.next=second

            prev=cur
            cur=nxtPair
        return dummy.next

        