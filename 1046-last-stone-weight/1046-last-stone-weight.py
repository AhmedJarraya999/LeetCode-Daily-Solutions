class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            #klebnehom khater minheap implemented
            if second>first:
                heapq.heappush(stones,first-second)
        stones.append(0)#au cas ou ferghet list 
        return abs(stones[0])
        
        