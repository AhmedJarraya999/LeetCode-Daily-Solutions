class Solution {
    long M = (long)1e9 + 7;

    public int countPartitions(int[] nums, int k) {
        int n = nums.length;

        long[] dp = new long[n + 1];
        dp[n] = 1; // Base case

        for (int i = n - 1; i >= 0; i--) {
            long count = 0;
            int minEl = Integer.MAX_VALUE;
            int maxEl = Integer.MIN_VALUE;

            for (int j = i; j < n; j++) {
                minEl = Math.min(minEl, nums[j]);
                maxEl = Math.max(maxEl, nums[j]);

                if (maxEl - minEl > k)
                    break;

                count = (count + dp[j + 1]) % M;
            }

            dp[i] = count;
        }

        return (int) dp[0];
    }
}
