class Solution {
public:
    bool f(vector<int>& visited, vector<int>& nums, int target, int start, int k, int currentSum) {
        if (k == 1) return true; // Only one subset left, no need to check further
        if (currentSum == target) return f(visited, nums, target, 0, k - 1, 0); // Found a valid subset, look for the next one

        for (int i = start; i < nums.size(); ++i) {
            if (!visited[i] && currentSum + nums[i] <= target) {
                visited[i] = 1;
                if (f(visited, nums, target, i + 1, k, currentSum + nums[i])) return true;
                visited[i] = 0; // Backtrack
            }
        }
        return false;
    }

    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) return false;
        int target = sum / k;
        vector<int> visited(nums.size(), 0);
        return f(visited, nums, target, 0, k, 0);
    }
};
