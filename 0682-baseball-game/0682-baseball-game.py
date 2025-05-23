class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for  val in operations:
            if val.lstrip('-').isdigit():
                stack.append(int(val))
            elif val=="+" and len(stack)>=2:
                latest=stack[-1]
                beforelatest=stack[-2]
                stack.append(latest+beforelatest)
            elif val=="D": 
                latest=stack[-1]
                stack.append(latest*2)
            elif val=="C":
                stack.pop()
        res=sum(stack)
        return res


        