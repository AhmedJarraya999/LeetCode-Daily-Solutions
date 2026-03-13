class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        state = 0   # 0: inc, 1: dec, 2: inc
        if nums[0]>=nums[1]:
             return False


        for i in range(2, n):
            if state == 0:
                if nums[i] > nums[i-1]:
                    continue
                elif nums[i] < nums[i-1]:
                    state = 1
                else:
                    return False

            elif state == 1:
                if nums[i] < nums[i-1]:
                    continue
                elif nums[i] > nums[i-1]:
                    state = 2
                else:
                    return False

            else:  # state == 2
                if nums[i] <= nums[i-1]:
                    return False

        return state == 2