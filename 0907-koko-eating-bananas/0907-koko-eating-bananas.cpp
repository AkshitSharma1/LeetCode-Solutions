class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(),piles.end());
        long long l=1;
        long long r = piles[piles.size()-1];
        long long ans=0;
        long long mid=0;
        while(l<=r) {
            long long timeToEat=0;

            mid = (l+r)/2;
            for(auto pile:piles) {
                timeToEat +=ceil((double)pile/mid);
            }
            if(timeToEat>h) {
                //Try increase eat speed
                l = mid+1;

            } else {
                //Decrease eat speed
                ans=mid;
                r=mid-1;
            }
        }
    return ans;
    }
};