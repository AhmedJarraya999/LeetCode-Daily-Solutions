class Solution(object):
    def hasCycle(self, head):
        visited_nodes=set()
        curr=head 
        while curr:
            if curr in visited_nodes:
                return True
            visited_nodes.add(curr)
            curr=curr.next
        return False
            
        