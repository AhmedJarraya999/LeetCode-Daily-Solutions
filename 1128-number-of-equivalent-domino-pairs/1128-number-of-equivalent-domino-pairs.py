class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count=defaultdict(int)
        result=0
        for a,b in dominoes:
            key = tuple(sorted((a, b)))
            result+=count[key]
            count[key]+=1
        return result
        