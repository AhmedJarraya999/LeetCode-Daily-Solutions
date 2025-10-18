class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        used=set()
        for num in nums:
            for val in range (num-k,num+k+1):
                if val not in used:
                    used.add(val)
                    break
        return len(used)


        