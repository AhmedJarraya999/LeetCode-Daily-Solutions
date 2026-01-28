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
            node.prev=cur
            cur.next=node
            cur=node
            ll.append(cur)
        heap=[]
        inversions=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inversions+=1
            heapq.heappush(heap,(nums[i]+nums[i-1],i-1,ll[i].prev))
        ops=0
        while inversions:
            while True:
                tot,i,left=heapq.heappop(heap)
                right=left.next
                if not left or not right or not right.alive:
                    continue
                if left.val+right.val!=tot:
                    continue
                break
            ##eliminate inversions
            if left.prev and left.prev.val>left.val:
                inversions-=1
            if left.next and left.next.val<left.val:
                inversions-=1
            if right.next and right.next.val<right.val:
                inversions-=1
            ##update ll with new values
            left.val=tot
            left.next=(right.next if right.next else None)
            right.alive=False
            if right.next:
                right.next.prev=left
            #check if new inversions are added
            if left.prev and left.prev.val>left.val:
                inversions+=1
            if left.next and left.next.val<left.val:
                inversions+=1
            ##push new formed adjacent pairs
            if left.prev:
                heapq.heappush(heap,(left.prev.val+left.val,left.prev.i,left.prev))
            if left.next:
                heapq.heappush(heap,(left.next.val+left.val,left.i,left))
            ops+=1
        return ops

      









 


