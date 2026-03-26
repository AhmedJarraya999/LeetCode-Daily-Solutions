class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:  
        n=len(nums)
        res= -inf
        i=0
        while i<n:
            #find shortest first segment
            j=i+1
            while j<n and nums[j]>nums[j-1]:
                j+=1
            p=j-1
            if p==i: ##length of cur segment is 0
                i+=1
                continue
            curr=nums[p]+nums[p-1]
            ##full second segment 
            while j<n and nums[j]<nums[j-1]:
                curr+=nums[j]
                j+=1
            q=j-1
            if p==q or q==n-1 or (q<n and nums[q]==nums[j]):
                i=q
                continue
            ##third segment with max sum
            curr+=nums[j]
            j+=1
            acc=0
            mx=0
            while j<n and nums[j]>nums[j-1]:
                acc+=nums[j]
                mx=max(mx,acc)
                j+=1
            curr+=mx
            ##maximise sum of first segment
            acc=0
            mx=0
            jj=p-2
            while jj>=0 and nums[jj]<nums[jj+1]:
                acc+=nums[jj]
                mx=max(mx,acc)
                jj-=1
            curr+=mx
            res=max(res,curr)
            i=q ##next possible trionic array starting with last segment 
        return res
            

        # n = len(nums)
        # i = 0
        # ans = -inf
        # while i < n:
        #     l = i
        #     i += 1
        #     while i < n and nums[i - 1] < nums[i]:
        #         i += 1
        #     if i == l + 1:
        #         continue

        #     p = i - 1
        #     s = nums[p - 1] + nums[p]
        #     while i < n and nums[i - 1] > nums[i]:
        #         s += nums[i]
        #         i += 1
        #     if i == p + 1 or i == n or nums[i - 1] == nums[i]:
        #         continue

        #     q = i - 1
        #     s += nums[i]
        #     i += 1
        #     mx = t = 0
        #     while i < n and nums[i - 1] < nums[i]:
        #         t += nums[i]
        #         i += 1
        #         mx = max(mx, t)
        #     s += mx

        #     mx = t = 0
        #     for j in range(p - 2, l - 1, -1):
        #         t += nums[j]
        #         mx = max(mx, t)
        #     s += mx

        #     ans = max(ans, s)
        #     i = q
        # return ans
# class Solution:
#     def maxSumTrionic(self, nums):
#         n = len(nums)
#         INF = float('-inf')

#         dp0 = [0]*n  # increasing
#         dp1 = [INF]*n  # decreasing
#         dp2 = [INF]*n  # increasing again

#         dp0[0] = nums[0]

#         for i in range(1, n):
#             # state 0: increasing
#             if nums[i] > nums[i-1]:
#                 dp0[i] = max(dp0[i-1] + nums[i], nums[i])
#             else:
#                 dp0[i] = nums[i]

#             # state 1: decreasing
#             if nums[i] < nums[i-1]:
#                 dp1[i] = dp1[i-1] + nums[i]
#                 dp1[i] = max(dp1[i], dp0[i-1] + nums[i])

#             # state 2: increasing again
#             if nums[i] > nums[i-1]:
#                 dp2[i] = dp2[i-1] + nums[i]
#                 dp2[i] = max(dp2[i], dp1[i-1] + nums[i])

#         return max(dp2)
# class Solution:
#     def maxSumTrionic(self, nums):
#         n = len(nums)

#         inc = nums[:]     # increasing ending at i
#         dec = nums[:]     # decreasing ending at i
#         incR = nums[:]    # increasing starting at i

#         # increasing left
#         for i in range(1, n):
#             if nums[i] > nums[i-1]:
#                 inc[i] = inc[i-1] + nums[i]

#         # decreasing left
#         for i in range(1, n):
#             if nums[i] < nums[i-1]:
#                 dec[i] = dec[i-1] + nums[i]

#         # increasing right
#         for i in range(n-2, -1, -1):
#             if nums[i] < nums[i+1]:
#                 incR[i] = incR[i+1] + nums[i]

#         res = float('-inf')

#         # pick q as valley
#         for q in range(1, n-1):
#             # must have a decreasing before and increasing after
#             if dec[q] == nums[q] or incR[q] == nums[q]:
#                 continue

#             # now find valid p before q
#             # we need inc[p] and dec[q] must connect

#             p = q - 1
#             if nums[p] > nums[q]:  # valid decreasing connection
#                 # ensure inc part exists
#                 if inc[p] != nums[p]:
#                     total = inc[p] + (dec[q] - nums[p]) + incR[q] - nums[q]
#                     res = max(res, total)

#         return res