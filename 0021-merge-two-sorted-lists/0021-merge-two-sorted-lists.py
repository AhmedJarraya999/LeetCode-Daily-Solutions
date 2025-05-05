class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # dummy node to simplify edge cases
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining part after one list ends
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
