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
            if nums[i]<nums[i-1]:
                inversions+=1
            heapq.heappush(heap,(nums[i]+nums[i-1],i-1,ll[i].prev))
        ops=0
        while inversions:
            while True:
                tot,i,left=heapq.heappop(heap)
                right=left.next
                if not left.alive or not right or not right.alive:
                    continue
                if tot!=left.val+right.val:
                    continue
                break
            # Before merging, decrease inversions that will be removed
            if left.prev and left.prev.val>left.val:
                inversions-=1
            if left.next and left.next.val<left.val:
                inversions-=1
            if right.next and right.val>right.next.val:
                inversions-=1

            right.alive=False
            left.val=tot
            left.next=right.next
            if right.next:
                right.next.prev=left
            #check if inversions are added
            if left.next and left.val>left.next.val:
                inversions+=1
            if left.prev and left.val<left.prev.val:
                inversions+=1
            #push new to heap
            if left.prev:
                heapq.heappush(heap,(left.prev.val+left.val,left.prev.i,left.prev))
            if left.next:
                heapq.heappush(heap,(left.next.val+left.val,left.i,left))
            ops+=1
        return ops






# class Node:
#     def __init__(self,val,i):
#         self.val=val
#         self.i=i
#         self.prev=None
#         self.next=None
#         self.alive=True
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         head=Node(nums[0],0)
#         cur=head
#         ll=[head]
#         for i in range(1,len(nums)):
#             node=Node(nums[i],i)
#             cur.next=node
#             node.prev=cur
#             cur=node
#             ll.append(cur)
#         inversions=0
#         heap=[]
#         for i in range(1,len(nums)):
#             if nums[i]<nums[i-1]:
#                 inversions+=1
#             heapq.heappush(heap,(nums[i]+nums[i-1],i-1,ll[i].prev))
#         ops=0
#         while inversions:
#             while True:
#                 tot,i,left=heapq.heappop(heap)
#                 right=left.next
#                 if not left.alive or not right or not right.alive:
#                     continue
#                 if left.val+right.val!=tot:
#                     continue
#                 break
#             ##check if inversion zeyda
#             if left.prev and left.prev.val>left.val:
#                 inversions-=1
#             if left.next and left.next.val<left.val:
#                 inversions-=1
#             if right.next and right.next.val<right.val:
#                 inversions-=1
 
#             #update left node
#             left.val=tot
#             left.next=(right.next if right.next else None)
#             right.alive=False
#             if right.next:
#                 right.next.prev=left
            
#             if left.next and left.val>left.next.val:
#                 inversions+=1
#             if left.prev and left.val<left.prev.val:
#                 inversions+=1

#             ##push new 
#             if left.prev:
#                 heapq.heappush(heap,(left.prev.val+left.val,left.prev.i,left.prev))
#             if left.next:
#                 heapq.heappush(heap,(left.val+left.next.val,left.i,left))
#             ops+=1
#         return ops

        




# class Node:
#     def __init__(self,val,i):
#         self.val=val
#         self.i=i
#         self.prev=None
#         self.next=None
#         self.alive=True
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         head=Node(nums[0],0)
#         cur=head
#         ll=[head]
#         for i in range(1,len(nums)):
#             node=Node(nums[i],i)
#             cur.next=node
#             node.prev=cur
#             cur=node
#             ll.append(cur)
#         heap=[]
#         inversions=0
#         for i in range(1,len(nums)):
#             if nums[i-1]>nums[i]:
#                 inversions+=1
#             heapq.heappush(heap,(nums[i]+nums[i-1],i-1, ll[i].prev))
#         ops=0
#         while inversions:
#             while True:
#                 tot,i,left=heapq.heappop(heap)
#                 right=left.next
#                 if not left.alive or not right or not right.alive:
#                     continue
#                 if left.val+right.val!=tot:
#                     continue
#                 break

#             ##check decreasing invrsions
#             if left.prev and left.prev.val>left.val:
#                 inversions-=1
#             if left.next and left.next.val<left.val:
#                 inversions-=1
#             if right.next and right.val>right.next.val:
#                 inversions-=1
#              ##check decreasing invrsions

#             ##links update
#             left.val=tot
#             right.alive=False
#             left.next=(right.next if right.next else None)
#             if right.next:
#                 right.next.prev=left
#             #links update

#             if  left.next and left.val>left.next.val:
#                 inversions+=1
#             if left.prev and left.val<left.prev.val:
#                 inversions+=1
#             #push new
#             if left.prev:
#                 heapq.heappush(heap,(left.prev.val+left.val,left.prev.i,left.prev))
#             if left.next:
#                 heapq.heappush(heap,(left.val+left.next.val,left.i,left))
#             #push new
#             ops+=1
#         return ops
            



# class Node:
#     def __init__(val,i):
#         self.val=val
#         self.i=i
#         self.prev=None
#         self.next=None
#         self.alive=True
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         head=Node(nums[0],0)
#         cur=head
#         ll=[head]
#         for i in range(1,len(nums)):
#             node=Node(nums[i],i)
#             cur.next=node
#             node.prev=cur
#             cur=node
#             ll.append(cur)
#         heap=[]
#         inversions=0
#         for i in range(1,len(nums)):
#             if nums[i]<nums[i-1]:
#                 inversions+=1
#             heapq.heappush(heap,(nums[i]+nums[i-1],i-1,nodes[i].prev))
#         while inversions:
#             while True:
#                 total,i,left=heapq.heappop(heap)
#                 right=left.next
#                 if not left.alive or not right or not right.alive:
#                     continue
#                 if left.val + right.val != total:
#                     continue
#                 break
#             if left.prev and left.prev>left.val:
#                 inversions-=1
#             if left.next and left.next<left.val:
#                 inversions-=1
#                 ##updating link
#             left.val=tot
#             right.alive=False
#             left.next=(right.next if right.next else None)
#             if right.next:
#                 right.next.prev = left
#                 ##updating link






# import heapq
# from typing import List


# class Node:
#     def __init__(self, val: int, i: int):
#         self.val = val
#         self.prev = None
#         self.next = None
#         self.alive = True  # for lazy deletion
#         self.i = i


# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         n = len(nums)

#         # build doubly linked list
#         head = Node(nums[0], 0)
#         curr = head
#         nodes = [head]

#         for i in range(1, n):
#             node = Node(nums[i], i)
#             curr.next = node
#             node.prev = curr
#             curr = node
#             nodes.append(node)

#         inversions = 0
#         heap = []

#         # count initial inversions and push adjacent pairs
#         for i in range(1, n):
#             if nums[i] < nums[i - 1]:
#                 inversions += 1
#             heapq.heappush(heap, (nums[i] + nums[i - 1], i - 1, nodes[i].prev))

#         ops = 0
#         while inversions:
#             # lazy deletion loop
#             while True:
#                 total, i, left = heapq.heappop(heap)
#                 right = left.next
#                 if not left.alive or not right or not right.alive:
#                     continue
#                 if left.val + right.val != total:
#                     continue
#                 break
# ## got it and wow 
#             # remove left-right related inversions
#             if left.prev and left.val < left.prev.val:
#                 inversions -= 1
#             if right.val < left.val:
#                 inversions -= 1
#             if right.next and right.next.val < right.val:
#                 inversions -= 1
# ## got it and wow 

#             # merge right into left
#             left.val = total
#             right.alive = False
#             left.next = right.next
#             if right.next:
#                 right.next.prev = left

#             # add new possible inversions
#             if left.prev and left.val < left.prev.val:
#                 inversions += 1
#             if left.next and left.next.val < left.val:
#                 inversions += 1

#             # push new adjacent pairs
#             if left.prev:
#                 heapq.heappush(heap, (left.prev.val + left.val, left.prev.i, left.prev))
#             if left.next:
#                 heapq.heappush(heap, (left.val + left.next.val, left.i, left))

#             ops += 1

#         return ops
