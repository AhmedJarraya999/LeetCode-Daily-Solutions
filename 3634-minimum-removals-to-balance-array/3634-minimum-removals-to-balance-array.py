# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         if len(nums)==1:
#             return 0
#         nums.sort()
#         i=0
#         j=1
#         while nums[j]<=k*nums[i] and j<len(nums)-2:
#             j+=1
#         return len(nums)-(j-i+1)
# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)

#         i = 0
#         max_len = 0

#         for j in range(n):
#             while nums[j] > k * nums[i]:
#                 i += 1
#             max_len = max(max_len, j - i + 1)


#         return n - max_len
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=0
        max_len=0
        while j<n:
            while nums[j]>k*nums[i]:
                i+=1
            max_len=max(max_len,j-i+1)
            j+=1
        return n-max_len
        
    

        # nums.sort()
        # n = len(nums)

        # i = 0
        # j = 0
        # max_len = 0

        # while j < n:
        #     while nums[j] > k * nums[i]:
        #         i += 1
        #     max_len = max(max_len, j - i + 1)
        #     j += 1

        # return n - max_len
