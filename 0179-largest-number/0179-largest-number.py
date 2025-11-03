class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        def compare(a,b):
            if a+b>b+a:
                return -1 #a should come first
            elif b+a>a+b:
                return 1 #b should come first
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == '0':
            return '0'
        return ''.join(nums)
            
       


        