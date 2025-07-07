class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # sort by start day
        min_heap = []
        day = 1
        i = 0
        n = len(events)
        count = 0

        while i < n or min_heap:
        # If no events are ongoing, skip to the next event's start day
            if not min_heap:
                 day = max(day, events[i][0])
        
                # Add all events starting today
            while i < n and events[i][0] <= day:
                  heapq.heappush(min_heap, events[i][1])
                  i += 1

                # Remove events that have already expired
            while min_heap and min_heap[0] < day:
                 heapq.heappop(min_heap)

                # Attend the event that ends earliest
            if min_heap:
                    heapq.heappop(min_heap)
                    count += 1
                    day += 1

        return count
        # events.sort(key=lambda x: (x[1], x[0]))
        # occupied=set()
        # for start,end in events:
        #     for day in range(start,end+1):
        #         if day not in occupied:
        #             occupied.add(day)
        #             break
        # return len(occupied)


        