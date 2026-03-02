class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c>target:
                return c
        return letters[0]
        # left,right=0,len(letters)
        # while left<right:
        #     mid=(left+right)//2
        #     if letters[mid]<=target:
        #         mid=left+1
        #     else:
        #         right=mid-1
        # if left=n:
        #     return letters[0]
        # else:
        #     return letters[left]






        # left, right = 0, len(letters) - 1
        # n = len(letters)
        
        # while left <= right:
        #     mid = (left + right) // 2
        #     if letters[mid] <= target:   
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # if left==n:
        #     return letters[0]
        # else:
        #     return letters[left] 