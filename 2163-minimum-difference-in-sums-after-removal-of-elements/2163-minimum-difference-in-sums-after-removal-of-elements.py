class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3

        # Step-1: Build right_maxsum array (stores the max sum of k elements from index i to n-1)
        min_heap = []
        right_sum = 0
        right_maxsum = [0] * n

        for i in range(n - 1, k - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i]
            if len(min_heap) > k:
                right_sum -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                right_maxsum[i] = right_sum

        # Step-2: Compute min-diff by traversing left part (0 to 2k-1)
        max_heap = []
        left_sum = 0
        min_diff = float('inf')

        for i in range(2 * k):
            heapq.heappush(max_heap, -nums[i])  # Using max-heap simulation
            left_sum += nums[i]
            if len(max_heap) > k:
                left_sum -= -heapq.heappop(max_heap)
            if len(max_heap) == k and i + 1 < n:
                min_diff = min(min_diff, left_sum - right_maxsum[i + 1])

        return min_diff
