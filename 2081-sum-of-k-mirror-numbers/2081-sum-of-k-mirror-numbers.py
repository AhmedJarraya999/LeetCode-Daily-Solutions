class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def to_base_k(x: int) -> str:
            if x == 0:
                return "0"
            digits = []
            while x > 0:
                digits.append(str(x % k))
                x //= k
            return ''.join(reversed(digits))

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def generate_palindromes():
            # Start with 1-digit palindromes
            length = 1
            while True:
                # Odd-length palindromes
                for half in range(10 ** (length - 1), 10 ** length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # Ex: 123 -> 12321

                # Even-length palindromes
                for half in range(10 ** (length - 1), 10 ** length):
                    s = str(half)
                    yield int(s + s[::-1])  # Ex: 123 -> 123321

                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_palindrome(to_base_k(num)):
                total += num
                count += 1
                if count == n:
                    break

        return total

# class Solution:
#     def kMirror(self, k: int, n: int) -> int:
#         def base_k(i: int, k: int):
#             res=""
#             while i>0:
#                 res=str(i%k)+res
#                 i//=k
#             return res
#         def is_palindrome(n: int) -> bool:
#             s = str(n)
#             return s == s[::-1]

#         cnt=0
#         i=1
#         output=0
#         while cnt<n:
#             if is_palindrome(base_k(i,k)) and is_palindrome(i):
#                 cnt+=1
#                 output+=i
#             i+=1
#         return output


        