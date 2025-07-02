class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_starting_point=sorted(trips,key=lambda x:x[1])
        minHeap=[]#ending position & num of passengers
        curPass=0
        #minHeap(ending_position,numPass)
        for t in  trips_starting_point:
            while minHeap and minHeap[0][0]<=t[1]:
                curPass-=minHeap[0][1]
                heapq.heappop(minHeap)

            curPass+=t[0]
            if curPass>capacity:
                return False
            heapq.heappush(minHeap,[t[2],t[0]])
        return True

        