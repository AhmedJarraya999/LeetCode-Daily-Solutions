class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        start=1
        for i in range(2,n+1):
            start=start*10+i
        ch=str(start)
        perms=sorted(["".join(p) for p in permutations(ch)])
        return perms[k-1]

