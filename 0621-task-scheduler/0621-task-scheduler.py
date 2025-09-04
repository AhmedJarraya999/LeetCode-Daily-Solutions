class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxHeap=[-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque()
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap) 
                #khatermaaousin famech minheap
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
                






        