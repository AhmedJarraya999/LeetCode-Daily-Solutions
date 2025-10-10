class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        int ans = INT_MIN; // Initialize with the smallest possible integer value

        // Iterate through possible starting points within the last 'k' elements
        for (int i = n - k; i < n; i++) {
            int current_sum = 0;
            // Calculate sum by jumping 'k' steps backward
            for (int j = i; j >= 0; j -= k) {
                current_sum += energy[j];
                ans = max(ans, current_sum); // Update maximum energy
            }
        }
        return ans;
    }
};