class Solution(object):
    def findEvenNumbers(self, digits):
        checker=set()
        for i in range(len(digits)):
            if digits[i]!=0:
                for j in range(len(digits)):
                    if i!=j:
                        for k in range(len(digits)):
                            if k!=i and j!=k and digits[k]%2==0:
                                checker.add(digits[i]*100+digits[j]*10+digits[k])
        return sorted(list(checker))
        
        