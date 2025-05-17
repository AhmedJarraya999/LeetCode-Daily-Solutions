class Solution(object):
    def assignTasks(self, servers, tasks):
        res = [0] * len(tasks)
        # array fiha server[i] qui correspend el weight w i howa l'index
        available = [(servers[i], i) for i in range(len(servers))]
        # transform it into a heap
        heapq.heapify(available)
        unavailable = []
        t = 0
        for i in range(len(tasks)):
            t = max(t, i)
            if len(available) == 0:
                t = unavailable[0][0]  # ✅ FIXED: get the next time a server becomes free
            while unavailable and t >= unavailable[0][0]:
                timeFree, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            weight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavailable, (t + tasks[i], weight, index))
        return res