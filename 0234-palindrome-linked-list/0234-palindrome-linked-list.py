class Solution(object):
    def isPalindrome(self, head):
        tab=[]
        while head:
            tab.append(head.val)
            head=head.next
        return tab==tab[::-1]
    
        