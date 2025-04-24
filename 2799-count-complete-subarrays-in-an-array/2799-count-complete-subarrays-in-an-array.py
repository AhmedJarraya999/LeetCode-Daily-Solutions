class Solution(object):
    def countCompleteSubarrays(self,nums):
        total_unique = len(set(nums))
        n = len(nums)
        count = 0
        left = 0
        freq = {}

        for right in range(n):
            num = nums[right]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            while len(freq) == total_unique:
                count += (n - right)  
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count
