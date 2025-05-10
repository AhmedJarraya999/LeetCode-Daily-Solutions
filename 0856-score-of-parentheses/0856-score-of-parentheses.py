class Solution(object):
    def scoreOfParentheses(self, s):
        score=1
        stack=[]
        output=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(0)
            elif s[i]==")":
                latest=stack.pop()
                if latest==0:
                    val=1
                else:
                    val=latest*2
                if not stack:
                    output+=val
                else:
                    stack[-1]+=val
        return output

 

        