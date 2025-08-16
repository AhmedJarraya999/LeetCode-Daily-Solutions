class Solution:
    def maximum69Number (self, num: int) -> int:
        ch=list(str(num))
        for i in range(len(ch)):
            if ch[i]!= '9':
                ch[i] = '9'
                break
        return int("".join(ch))


        