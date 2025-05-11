class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr)):
            if( (i>=2) and  (arr[i]%2!=0) and (arr[i-1]%2!=0) and (arr[i-2]%2!=0) ):
                return True
        return False
