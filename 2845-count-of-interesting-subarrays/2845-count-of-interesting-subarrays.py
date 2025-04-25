class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        countMap = defaultdict(int)
        countMap[0] = 1  # for subarrays starting at index 0
        result = 0
        prefixCount = 0

        for num in nums:
            if num % modulo == k:
                prefixCount += 1
            
        # Calculate what previous prefix count would make this subarray interesting
            target = (prefixCount - k + modulo) % modulo
            result += countMap[target]

            # Update hashmap
            countMap[prefixCount % modulo] += 1

        return result
            
        