class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        eng=[]
        for eff,spd in zip(efficiency,speed):
            eng.append([eff,spd])
        #sort by decending order efficiency
        eng.sort(reverse=True)
        #keep track of res and total speed as far
        res,speed=0,0
        minHeap=[]
        for eff,spd in eng:
            if len(minHeap)==k:
                speed-=heapq.heappop(minHeap)
            speed+=spd
            heapq.heappush(minHeap,spd)
            res=max(res,eff*speed)
        return res %(10**9+7)


        