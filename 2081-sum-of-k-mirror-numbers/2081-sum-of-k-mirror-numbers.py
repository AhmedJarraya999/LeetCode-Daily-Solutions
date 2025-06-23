class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def base_k(i: int, k: int):
            # res=""
            # while i>0:
            #     res=str(i%k)+res
            #     i//=k
            # return res
            if i == 0:
                return "0"
            digits = []
            while i > 0:
                 digits.append(str(i % k))  
                 i //= k
            return ''.join(reversed(digits))  
        def is_palindrome(n: int) -> bool:
            s = str(n)
            return s == s[::-1]

        cnt=0
        i=1
        output=0
        while cnt<n:
            if is_palindrome(base_k(i,k)) and is_palindrome(i):
                cnt+=1
                output+=i
            i+=1
        return output


        