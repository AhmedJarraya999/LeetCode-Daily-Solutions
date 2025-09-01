class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #infection of adding 1 student on ration per class
        def gain(p,t):
            return (p+1)/(t+1) -p/t
        heap=[(-gain(p, t), p, t)  for p,t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            g,p,t=heapq.heappop(heap)
            p,t=p+1,t+1
            heapq.heappush(heap,(-gain(p,t),p,t))
        tot_ratio=sum(p/t for _,p,t in heap)
        return tot_ratio/len(classes)

        