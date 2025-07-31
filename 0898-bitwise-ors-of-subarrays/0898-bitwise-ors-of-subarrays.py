class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        prev = set()
        
        for x in arr:
            cur = {x}
            for y in prev:
                cur.add(x | y)
            res.update(cur)
            prev = cur
        
        return len(res)
