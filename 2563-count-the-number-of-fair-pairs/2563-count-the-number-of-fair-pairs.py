class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        def bin_search(l,r,target):
            while l<=r:
                m=(l+r)//2
                if nums[m]>=target:
                    r=m-1
                else:
                    l=m+1
            return r 


        nums.sort()
        counter=0
        for i in range(len(nums)):
            lowBound=lower-nums[i]
            upBound=upper-nums[i]
            counter+= ( bin_search(i+1,len(nums)-1,upBound +1)-
            bin_search(i+1,len(nums)-1,lowBound))
        return counter
    
        