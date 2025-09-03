class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=0
        myset=defaultdict(int)
        for t in tasks:
            myset[t]+=1
        max_freq=max(myset.values())
        count_of_max_freq_tasks = sum(1 for v in myset.values() if v == max_freq)
        answer = max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq_tasks)
        return answer




        




        