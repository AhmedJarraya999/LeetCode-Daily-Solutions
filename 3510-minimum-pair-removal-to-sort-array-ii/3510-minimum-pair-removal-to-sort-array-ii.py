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
        for i in range(1,len(nums)):
            heapq.heappush(heap,(nums[i]+nums[i-1],i-1,ll[i].prev))
            if nums[i]<nums[i-1]:
                inversions+=1
        ops=0
        while inversions!=0:
            while True:
                tot,i,left=heapq.heappop(heap)
                right=left.next
                if not left.alive or not right or not right.alive:
                    continue
                if tot!=left.val+left.next.val:
                    continue
                break
            ##check  decrase inversions
            if left.prev and left.prev.val>left.val:
                inversions-=1
            if left.next and left.next.val<left.val:
                inversions-=1
            if right.next and right.next.val<left.val:
                inversions-=1
            #mise a jour link ll
            left.val=tot
            right.alive=False
            left.next=(right.next if right.next else None)
            if right.next:
                right.next.prev=left
            ##famechi 9albeet jdod 
            if left.next and left.next.val<left.val:
                inversions+=1
            if left.prev and left.prev.val>left.val:
                inversions+=1
            #push new value to the heap
            if left.prev:
                heapq.heappush(heap,(left.prev.val+left.val,left.prev.i,left.prev))
            if left.next:
                heapq.heappush(heap,(left.next.val+left.val,left.i,left))
            ops+=1
        return ops

            


        






 


