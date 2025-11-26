class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        lowest=nums[0]
        biggest=nums[n-1]
        g=gcd(biggest,lowest)
        return g
        