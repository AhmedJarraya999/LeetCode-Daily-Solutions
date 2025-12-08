from collections import deque

class Solution:
    def countPartitions(self, nums, k):
        n = len(nums)
        MOD = 10**9 + 7
        dp=[1]+[0]*n
        acc=1
        sl=SortedList()
        l=0
        for r in range(n):
            sl.add(nums[r])
            while sl[-1]-sl[0]>k:
                sl.remove(nums[l])
                acc=(acc-dp[l])% MOD
                l+=1
            dp[r+1]=acc
            acc= (acc+dp[r+1])%MOD
        return dp[n]


        # # dp[i] = number of partitions starting at index i
        # dp = [0] * (n + 1)
        # dp[n] = 1  # base case: one way to partition an empty suffix

        # # prefix sums: pref[i] = dp[i] + dp[i+1] + ... + dp[n]
        # pref = [0] * (n + 2)
        # pref[n] = dp[n]
        # pref[n+1] = 0

        # maxdq = deque()
        # mindq = deque()

        # j = n - 1

        # # We process i from right to left
        # for i in range(n - 1, -1, -1):

        #     # Make sure j >= i
        #     if j < i:
        #         j = i
        #         maxdq.clear()
        #         mindq.clear()

        #     # Extend j while valid
        #     while j < n:

        #         # Insert nums[j] into max deque
        #         while maxdq and nums[maxdq[-1]] <= nums[j]:
        #             maxdq.pop()
        #         maxdq.append(j)

        #         # Insert nums[j] into min deque
        #         while mindq and nums[mindq[-1]] >= nums[j]:
        #             mindq.pop()
        #         mindq.append(j)

        #         # Check validity
        #         if nums[maxdq[0]] - nums[mindq[0]] > k:
        #             # Remove nums[j] because this last extension broke validity
        #             # Remove j from deques if present
        #             if maxdq and maxdq[-1] == j:
        #                 maxdq.pop()
        #             if mindq and mindq[-1] == j:
        #                 mindq.pop()
        #             break

        #         j += 1

        #     # Now valid window is [i ... j-1]

        #     # dp[i] = pref[i+1] - pref[j+1]
        #     dp[i] = (pref[i+1] - pref[j+1]) % MOD

        #     # Add dp[i] to prefix sum
        #     pref[i] = (dp[i] + pref[i+1]) % MOD

        #     # Before moving to i-1, remove i from deque if needed
        #     if maxdq and maxdq[0] == i:
        #         maxdq.popleft()
        #     if mindq and mindq[0] == i:
        #         mindq.popleft()

        # return dp[0] % MOD
