class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        mymap=defaultdict(int)
        for num in nums:
            mymap[num]+=1
        for key,value in mymap.items():
            if value==2:
                res.append(key)
            if len(res)==2:
                break
        return res