class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        answer=[0] * n
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev_index=stack.pop()
                answer[prev_index]=i-prev_index
            stack.append(i)
        return answer
        