class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        for n in nums:
            max_or |=n
        res=0
        def dfs(i,cur_or):
            nonlocal res,max_or
            if i==len(nums):
                res+=1 if cur_or==max_or else 0
                return
            #skip i
            dfs(i+1,cur_or)
            #include i
            dfs(i+1,cur_or|nums[i])
        dfs(0,0)
        return res