import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ops=0
        n=len(nums)
        left=[-1]*n
        right=[-1]*n
        alive=[True]*n
        for i in range(n):
            if i>0:
                left[i]=i-1
            if i<n-1:
                right[i]=i+1
        heap=[]
        for i in range(len(nums)-1):
            heapq.heappush(heap,(nums[i]+nums[i+1],i,i+1))
        op=0
        def is_sorted():
            prev = None
            for i in range(n):
                if alive[i]:
                    if prev is not None and prev > nums[i]:
                        return False
                    prev = nums[i]
            return True
        while not is_sorted():
            while heap:
                s,i,j=heapq.heappop(heap)
                if not alive[i] or not alive[j] or right[i]!=j:
                    continue
                nums[i]+=nums[j]
                alive[j]=False
                L=left[i]
                R=right[j]
                right[i] = R
                if R != -1:
                    left[R] = i
                
                # Push new adjacent sums
                if L != -1:
                    heapq.heappush(heap, (nums[L] + nums[i], L, i))
                if R != -1:
                    heapq.heappush(heap, (nums[i] + nums[R], i, R))
                ops+=1
                break
        return ops
        
