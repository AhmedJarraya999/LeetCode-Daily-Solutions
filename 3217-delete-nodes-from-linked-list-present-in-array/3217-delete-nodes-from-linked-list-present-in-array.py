# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        myset=set(nums)
        dummy=ListNode(0,head)
        prev=dummy
        curr=head
        while prev.next: 
            if curr.val in myset:
                prev.next= prev.next.next
            else:
                prev=prev.next
        return dummy.next
        