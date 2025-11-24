class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        cur=0
        for bit in nums:
            cur= (cur*2+bit)
            if cur%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        