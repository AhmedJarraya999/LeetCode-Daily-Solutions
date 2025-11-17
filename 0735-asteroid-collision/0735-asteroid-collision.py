class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            while stack and stack[-1]>0 and a<0:
                diff=a+stack[-1]
                if diff<0:
                    stack.pop()
                elif diff>0:
                    a=0  #stop the loop
                else:
                    a=0
                    stack.pop()
            if a: 
                stack.append(a)
        return stack
        # stack=[]
        # for a in asteroids:
        #     while stack and stack[-1]>0 and a<0:
        #         if stack[-1]<-a:
        #             stack.pop()
        #             continue
        #         elif stack[-1]==-a:
        #                 stack.pop() 
        #         break
        #     else:
        #         stack.append(a)
        # return stack


        