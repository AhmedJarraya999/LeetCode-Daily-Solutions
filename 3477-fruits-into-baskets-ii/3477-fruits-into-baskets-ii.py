class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used_b=set()
        res=0
        for i in range(len(fruits)):
            used_f=0
            for j in range(len(baskets)):
                if j in used_b or fruits[i]>baskets[j]:
                    continue
                used_b.add(j)
                used_f=1
                break
            if  not used_f:res+=1
        return res
                

                
        