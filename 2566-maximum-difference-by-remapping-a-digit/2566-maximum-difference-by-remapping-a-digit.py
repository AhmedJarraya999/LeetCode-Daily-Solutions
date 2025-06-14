class Solution:
    def minMaxDifference(self, num: int) -> int:
        diff=0
        digits=[int(d) for d in str(num)]
        maxlist=digits.copy()
        minlist=digits.copy()
        for i in range(len(digits)):
            if digits[i]!=0:
                val=digits[i]
                minlist=[0 if x==val  else x  for x in digits]
                break
            else:
                minlist=digits.copy()
        for i in range(len(digits)):
            if digits[i]!=9:
                val=digits[i]
                maxlist=[9 if x==val else x for x in digits]
                break
            else:
                maxlist=digits.copy()
        highest=int("".join(map(str,maxlist)))
        lowest=int("".join(map(str,minlist)))
        return highest-lowest






        