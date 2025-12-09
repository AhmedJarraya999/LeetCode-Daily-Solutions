class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD=10**9+7
        right=Counter(nums)
        left=Counter()
        ans = 0
        for j in range(len(nums)):
            right[nums[j]]-=1
            if right[nums[j]]==0:
                del(right[nums[j]])
            left_count = left.get(nums[j] * 2, 0)
            right_count = right.get(nums[j] * 2, 0)
            ans += left_count * right_count
            left[nums[j]] += 1
        return ans % MOD



        