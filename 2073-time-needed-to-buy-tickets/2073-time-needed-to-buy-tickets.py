class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        time = 0

        for i, t in enumerate(tickets):
            if i <= k:
                time += min(t, target)
            else:
                time += min(t, target - 1)

        return time
