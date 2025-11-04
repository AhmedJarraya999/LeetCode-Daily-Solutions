class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        freq = Counter(nums[:k])
        res=[]
        def compute_x_sum():
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            top_x = sorted_items[:x]
            return sum(num * count for num, count in top_x)
            sorted_items=sorted(freq.items(),key=lambda p:(-p[1],-p[0]))
            top_x=sorted_items[:x]
            return sum (num* count for num,count in top_x)
        res.append(compute_x_sum())
        for i in range(k,n):
            left=nums[i-k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            right = nums[i]
            freq[right] += 1
            res.append(compute_x_sum())
        return res


        