class Solution(object):
    def countAndSay(self, n):
        def rle(s):
            res=""
            counter=1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    counter+=1
                else:
                    res+=str(counter)+s[i-1]
                    counter=1
            res += str(counter) + s[-1]
            return res
        result = "1"
        for _ in range(n-1):
            result=rle(result)
        return(result)
        


        