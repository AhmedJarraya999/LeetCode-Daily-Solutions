class Solution(object):
    def calculate(self, s):
        s = s.replace(" ", "")  # remove spaces
        cur = 0
        prev = 0
        res = 0
        cur_op = 1 #1 means plus operation
        i = 0
        stack=[]
        for char in s:
            #digit condition
            if char.isdigit():
                #parse the number
                cur=cur*10+int(char)
            #opration condition
            elif char in ["+","-"]:
                res+=cur_op*cur
                cur_op=1 if char=="+" else -1
                cur=0
            #parentheses cndition
            elif char=="(":
                stack.append(res)
                stack.append(cur_op)
                cur_op=1
                res=0
            elif char==")":
                res+=cur_op*cur
#we multiply by the last sign appeneded to the stack before performing parentheses
                res*=stack.pop()
                res+=stack.pop()
                cur=0
        return res+cur_op*cur


        