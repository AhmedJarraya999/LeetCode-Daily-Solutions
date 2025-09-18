import heapq

class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.taskMap = {}  # taskId -> (userId, priority)
        self.heap = []     # max-heap by (-priority, -taskId, taskId)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.taskMap[taskId]
        self.taskMap[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId = heapq.heappop(self.heap)
            if taskId in self.taskMap:
                userId, curPriority = self.taskMap[taskId]
                # Ensure priority matches current one
                if curPriority == -priority:
                    del self.taskMap[taskId]
                    return userId
        return -1
