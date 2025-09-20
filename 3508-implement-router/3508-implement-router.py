from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO queue for packets
        self.packet_set = set()  # for duplicate detection
        self.dest_map = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False  # duplicate

        # If memory full, evict oldest packet
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_ts = self.queue.popleft()
            self.packet_set.remove((old_src, old_dst, old_ts))
            # remove old timestamp from dest_map
            arr = self.dest_map[old_dst]
            idx = bisect.bisect_left(arr, old_ts)
            if idx < len(arr) and arr[idx] == old_ts:
                arr.pop(idx)

        # Add new packet
        self.queue.append((source, destination, timestamp))
        self.packet_set.add(key)
        self.dest_map[destination].append(timestamp)  # timestamps always increasing
        return True

    def forwardPacket(self) -> list:
        if not self.queue:
            return []

        src, dst, ts = self.queue.popleft()
        self.packet_set.remove((src, dst, ts))

        # remove timestamp from destination list
        arr = self.dest_map[dst]
        idx = bisect.bisect_left(arr, ts)
        if idx < len(arr) and arr[idx] == ts:
            arr.pop(idx)

        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.dest_map[destination]
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)
        return right - left
