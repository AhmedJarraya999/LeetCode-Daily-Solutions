class Solution(object):
    def countLargestGroup(self, n):
        digit_sum_groups = {}

        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            if digit_sum in digit_sum_groups:
                digit_sum_groups[digit_sum] += 1
            else:
                digit_sum_groups[digit_sum] = 1

        max_group_size = max(digit_sum_groups.values())
        return sum(1 for size in digit_sum_groups.values() if size == max_group_size)
        