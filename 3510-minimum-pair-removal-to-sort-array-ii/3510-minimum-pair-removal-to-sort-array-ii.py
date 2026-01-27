class Node:
    def __init__(self,val,i):
        self.val=val
        self.i=i
        self.prev=None
        self.next=None
        self.alive=True


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head=Node(nums[0],0)
        cur=head
        ll=[head]
        for i in range(1,len(nums)):
            node=Node(nums[i],i)
            cur.next=node
            node.prev=cur
            cur=node
            ll.append(cur)

        heap=[]
        inversions=0
        ops=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                inversions+=1
            heapq.heappush(heap,(nums[i]+nums[i-1],i-1,ll[i].prev))
        while inversions:
            ##lazy deletion
            while True:
                tot,i,left=heapq.heappop(heap)
                right=left.next
                if not left.alive or not right or not right.alive:
                    continue
                if tot!=left.val+left.next.val:
                    continue
                break
            ###decreasiong inversions
            if left.prev and left.prev.val>left.val:
                inversions-=1
            if  left.next and left.next.val<left.val:
                inversions-=1
            if right.next and right.val>right.next.val:
                inversions-=1
            ##update links
            left.val=tot
            left.next=right.next
            if right.next:
                right.next.prev=left
            right.alive=False
            ##check if new inversions are added
            if left.prev and left.val<left.prev.val:
                inversions+=1
            if left.next and left.next.val<left.val:
                inversions+=1
            ##merge
            if left.prev:
                heapq.heappush(heap,(left.val+left.prev.val,left.prev.i,left.prev))
            if left.next:
                heapq.heappush(heap,(left.val+left.next.val,left.i,left))
            ops+=1
        return ops 
            






 


