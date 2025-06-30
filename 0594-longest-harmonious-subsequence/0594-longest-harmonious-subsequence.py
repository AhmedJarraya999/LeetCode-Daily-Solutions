class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter=Counter(nums)
        max_length=0
        for num in counter:
            if num+1 in counter:
                max_length=max(max_length,counter[num]+counter[num+1])
        return max_length 

        