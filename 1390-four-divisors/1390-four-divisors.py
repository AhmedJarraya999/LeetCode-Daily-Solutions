class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            divisors = []

            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisors.append(i)
                    if i != num // i:
                        divisors.append(num // i)

                if len(divisors) > 4:
                    break

                i += 1

            if len(divisors) == 4:
                total += sum(divisors)

        return total

# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         finallist = []

#         for num in nums:
#             cur = []
#             for i in range(1, num + 1):
#                 if num % i == 0:
#                     cur.append(i)

#             if len(cur) == 4:
#                 finallist.append(sum(cur))
#                 cur = []

#         return sum(finallist)
