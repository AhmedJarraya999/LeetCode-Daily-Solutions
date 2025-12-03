import math
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # 1) count how many points per y
        ycount = defaultdict(int)
        for x, y in points:
            ycount[y] += 1

            # 2) for each y compute number of segments (pairs) on that horizontal line
        pairs = []
        for y, c in ycount.items():
            if c >= 2:
                # pairs.append(c * (c - 1) // 2)
                pairs.append(math.comb(c, 2))

            # 3) accumulate trapezoid count by combining pairs from different levels

        ####simple 2 loops
        # result = 0
        # for i in range(len(pairs)):
        #     for j in range(i):
        #           result = (result + pairs[i] * pairs[j]) % MOD
        # return result
        ###ACCumulative trick
        result = 0
        acc = 0  # sum of pairs from previous levels
        for p in pairs:
            result = (result + acc * p) % MOD
            acc = (acc + p) % MOD

        return result
            