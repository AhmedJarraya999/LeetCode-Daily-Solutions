class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr)):
            if( (arr[i]%2!=0) and (arr[i-1]%2!=0) and (arr[i-2]%2!=0)  and (i>=2)):
                return True
        return False
