import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        freeRooms = list(range(n))
        heapq.heapify(freeRooms)
        
        busyRooms = []  # (endTime, room)
        count = [0] * n
        
        for start, end in meetings:
            # Free rooms that are done before current meeting
            while busyRooms and busyRooms[0][0] <= start:
                _, room = heapq.heappop(busyRooms)
                heapq.heappush(freeRooms, room)
            
            duration = end - start
            
            if freeRooms:
                room = heapq.heappop(freeRooms)
                heapq.heappush(busyRooms, (end, room))
            else:
                endTime, room = heapq.heappop(busyRooms)
                heapq.heappush(busyRooms, (endTime + duration, room))
            
            count[room] += 1
        
        return count.index(max(count))
