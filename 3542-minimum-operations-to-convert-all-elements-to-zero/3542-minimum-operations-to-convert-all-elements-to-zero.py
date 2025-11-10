class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        stack=[]
        for num in nums:
            while stack and stack[-1]>num:
                stack.pop() 
            if  num>0 and (not stack or num!=stack[-1]):
                count+=1
                stack.append(num)
        return count





        