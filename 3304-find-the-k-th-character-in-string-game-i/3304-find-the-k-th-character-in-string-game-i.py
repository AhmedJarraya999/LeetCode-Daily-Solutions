class Solution:
    def kthCharacter(self, k: int) -> str:
        # ones = bin(k - 1).count('1')
        # return chr(ord('a') + ones)
        res=['a']
        while len(res)<k:
            curr=res[:] #copy
            for i in range(len(curr)):
                if curr[i]=="z":
                    curr[i]="a"
                else:
                    curr[i]=chr(ord(curr[i])+1)
            res+=curr
        return res[k-1]

        