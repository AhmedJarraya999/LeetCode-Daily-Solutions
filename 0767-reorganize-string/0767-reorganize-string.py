class Solution(object):
    def reorganizeString(self, s):
        counter=Counter(s)
        # we will heapifyy based on the counter that is why cnt is first
        maxHeap=[[-cnt,char] for char,cnt in counter.items()]
        heapq.heapify(maxHeap) 
        prev=None
        res=""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt,char=heapq.heappop(maxHeap)
            res+=char
            cnt+=1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev=None
            if cnt!=0:
                prev=[cnt,char]
        return res

        