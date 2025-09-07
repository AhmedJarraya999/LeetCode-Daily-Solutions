class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myset=defaultdict(int)
        for num in nums:
            myset[num]+=1
        return max(myset,key=myset.get)