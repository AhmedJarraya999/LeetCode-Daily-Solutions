import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort meetings by start time
        free_rooms = list(range(n))  # All rooms are initially free
        heapq.heapify(free_rooms)

        busy_rooms = []  # Min-heap of (end_time, room_id)
        room_meet_count = [0] * n  # Number of meetings per room

        for start, end in meetings:
            # Free up rooms that have become available
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_id = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_id)
            
            if free_rooms:
                # Use the room with the smallest id
                room_id = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room_id))
            else:
                # No room is free; delay the meeting to the earliest end_time
                earliest_end_time, room_id = heapq.heappop(busy_rooms)
                delay = end - start
                new_end = earliest_end_time + delay
                heapq.heappush(busy_rooms, (new_end, room_id))

            room_meet_count[room_id] += 1

        # Find the room with the most meetings (min index in case of tie)
        max_meetings = max(room_meet_count)
        for i in range(n):
            if room_meet_count[i] == max_meetings:
                return i
