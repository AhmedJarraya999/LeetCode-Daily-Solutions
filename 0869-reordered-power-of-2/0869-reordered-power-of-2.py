class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        map=defaultdict(int)
        s=str(n)
        for val in s:
            map[val]+=1
        curr=1
        while curr<=10**9:
            map2=defaultdict(int)
            s2=str(curr)
            for x in s2: map2[x]+=1
            if map==map2: return True
            curr*=2
        return False

        