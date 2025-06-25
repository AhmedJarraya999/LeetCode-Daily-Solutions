from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLE(x):
            count = 0
            # a > 0
            for a in pos1:
                t = x // a
                count += bisect_right(nums2, t)
            # a < 0
            for a in neg1:
                t = x // a
                count += len(nums2) - bisect_left(nums2, t + (1 if x % a != 0 else 0))
            # a == 0
            if x >= 0:
                count += len(zero1) * len(nums2)
            return count

        # Preprocess nums1
        neg1 = [a for a in nums1 if a < 0]
        pos1 = [a for a in nums1 if a > 0]
        zero1 = [a for a in nums1 if a == 0]

        nums2.sort()  # safety, already sorted in problem

        low, high = -10**10, 10**10
        while low < high:
            mid = (low + high) // 2
            if countLE(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
