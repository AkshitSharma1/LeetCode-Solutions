class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
       // sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int minRadius = 0;
        
        for (auto house : houses) {
            auto minRad1 = lower_bound(heaters.begin(), heaters.end(), house);
            int temp = INT_MAX;
            
            if (minRad1 != heaters.end()) {
                temp = min(temp, abs(house - *minRad1));
            }
            if (minRad1 != heaters.begin()) {
                auto minRad2 = minRad1 - 1;
                temp = min(temp, abs(house - *minRad2));
            }
            
            minRadius = max(minRadius, temp);
        }
        
        return minRadius;
    }
};
