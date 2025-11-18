class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        ans=[-1]*n
        stack=[]
        index_map={value:index for index,value in enumerate(nums1)}
        for num in nums2:
            while stack and stack[-1]<num:
                el=stack.pop()
                if el in index_map:
                    ans[index_map[el]]=num
            stack.append(num)
        return ans
            


        