class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxHeap=[-x for x in target]
        heapq.heapify(maxHeap)
        total_sum=sum(target)
        while True:
            max_val = -heapq.heappop(maxHeap)
            rest_sum = total_sum - max_val
            #condition
            if max_val == 1 or rest_sum == 1:
                 return True
            #condition
            if rest_sum == 0 or max_val <= rest_sum:
                 return False

            prev_val = max_val % rest_sum
            if prev_val == 0:
                return False
            heapq.heappush(maxHeap, -prev_val)
            total_sum = rest_sum + prev_val

        
        