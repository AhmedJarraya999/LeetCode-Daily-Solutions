class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # Outer loop: starting index of the first subarray
        for i in range(n - 2 * k + 1):  # we need room for 2*k elements
            # Check first subarray [i .. i+k-1]
            first_inc = True
            for x in range(i, i + k - 1):
                if nums[x] >= nums[x + 1]:
                    first_inc = False
                    break
            
            if not first_inc:
                continue  # no need to check next subarray
            
            # Check the adjacent subarray [i+k .. i+2k-1]
            second_inc = True
            for x in range(i + k, i + 2 * k - 1):
                if nums[x] >= nums[x + 1]:
                    second_inc = False
                    break
            
            if first_inc and second_inc:
                return True
        
        return False
