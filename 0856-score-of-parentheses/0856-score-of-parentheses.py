class Solution(object):
    def scoreOfParentheses(self, s):
        stack=[]
        res=0
        val=0
        for i in range (len(s)):
            if s[i]=="(":
                stack.append(0)
            else:
                latest=stack.pop()
                if latest==0:
                    val=1
                else:
                    val=latest *2
                if not stack:
                    res+=val
                else:
                    stack[-1]+=val
        return res


 

        