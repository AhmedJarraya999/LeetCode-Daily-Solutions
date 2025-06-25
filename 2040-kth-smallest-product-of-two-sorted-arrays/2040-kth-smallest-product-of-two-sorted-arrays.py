class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLE(x):
            count = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        count += len(nums2)
                elif a > 0:
                    l, r = 0, len(nums2)
                    while l < r:
                        m = (l + r) // 2
                        if a * nums2[m] <= x:
                            l = m + 1
                        else:
                            r = m
                    count += l
                else:  
                    l, r = 0, len(nums2)
                    while l < r:
                        m = (l + r) // 2
                        if a * nums2[m] <= x:
                            r = m
                        else:
                            l = m + 1
                    count += len(nums2) - l
            return count
        
        low, high = -10**10, 10**10
        while low < high:
            mid = (low + high) // 2
            if countLE(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
