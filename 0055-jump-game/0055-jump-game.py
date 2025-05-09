class Solution(object):
    def canJump(self, nums):
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False





        def can_jump_from_position(position,nums):
            if position==len(nums)-1:
                return True
            furthest_jump=min(position+nums[position],len(nums)-1)
            for next_position in range (position+1,furthest_jump+1):
                if can_jump_from_position(next_position,nums):
                    return True
            return False
        return can_jump_from_position(0, nums)
        
        
        