class Solution(object):
    def findValidPair(self, s):
        digitCount=Counter(s)
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                verifdigit1=digitCount[s[i]]==int(s[i])
                verifdigit2=digitCount[s[i+1]]==int(s[i+1])
                if verifdigit1 and verifdigit2:
                    return s[i]+s[i+1]
        return ""
        