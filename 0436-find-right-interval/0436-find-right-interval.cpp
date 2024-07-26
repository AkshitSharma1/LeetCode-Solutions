#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> ans(n, -1);
        vector<pair<int, int>> startPoints; 

        for (int i = 0; i < n; ++i) {
            startPoints.push_back({intervals[i][0], i});
        }

        sort(startPoints.begin(), startPoints.end());

        for (int i = 0; i < n; ++i) {
            int endValue = intervals[i][1];
            auto it = lower_bound(startPoints.begin(), startPoints.end(), make_pair(endValue, 0));
            if (it != startPoints.end()) {
                ans[i] = it->second;
            }
        }

        return ans;
    }
};
