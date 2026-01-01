class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        cond=False
        for i in range(n-1,-1,-1):
                if digits[i]!=9:
                    digits[i]+=1
                    cond=True
                    break
                else:
                    digits[i]=0
        if cond==False:
            digits.insert(0, 1)
        return digits
            
        