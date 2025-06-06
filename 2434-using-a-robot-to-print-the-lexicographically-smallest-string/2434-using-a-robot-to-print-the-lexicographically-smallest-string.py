class Solution:
    def robotWithString(self, s: str) -> str:
        counter=Counter(s)
        stack=[]
        smallest='a'
        result=[]
        for c in s:
            stack.append(c)
            counter[c]-=1
            while smallest<='z' and counter[smallest]==0:
                smallest=chr(ord(smallest)+1)
            # Greedily pop from stack if it's <= smallest remaining
            while stack and stack[-1] <= smallest:
                result.append(stack.pop())
        # Pop remaining characters
        while stack:
            result.append(stack.pop())
        return ''.join(result)







