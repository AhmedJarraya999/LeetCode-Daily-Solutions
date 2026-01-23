from heapq import heappush, heappop

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        val = [num for num in nums]

        left = [i-1 for i in range(n)]
        right = [i+1 for i in range(n)]

        # Min-heap of [sum, index]
        pq = []
        unsorted = 0

        for i in range(n-1):
            heappush(pq, (val[i]+val[i+1], i))
            if val[i] > val[i+1]:
                unsorted += 1

        ans = 0

        while unsorted > 0 and pq:
            curr_sum, i = heappop(pq)
            j = right[i]

            # lazy removal
            if j >= n or left[j] != i or val[i] + val[j] != curr_sum:
                continue

            # valid pair
            if val[i] > val[j]:
                unsorted -= 1

            prev = left[i]
            next_ = right[j]

            if prev != -1 and val[prev] > val[i]:
                unsorted -= 1

            if next_ != n and val[j] > val[next_]:
                unsorted -= 1

            # merging
            val[i] = curr_sum
            right[i] = next_
            if next_ != n:
                left[next_] = i

            ans += 1

            # update heap with new adjacent pairs
            if prev != -1:
                if val[prev] > val[i]:
                    unsorted += 1
                heappush(pq, (val[prev] + val[i], prev))

            if next_ != n:
                if val[i] > val[next_]:
                    unsorted += 1
                heappush(pq, (val[i] + val[next_], i))

        return ans
