class Solution(object):
    def maxProduct(self, n):
        res=float('-inf')
        digits=[int(d)for d in str(n)]
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                res=max(res,digits[i]*digits[j])
        return res
                
            
        