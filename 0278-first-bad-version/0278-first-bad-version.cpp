// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long l =0;
         long long r = n;
         long long mid;
         long long ans=INT_MAX;
        while(l<=r) {
            mid = (l+r)/2;
            if(isBadVersion(mid)) {
                //Minimize search space
                ans = min(ans,mid);
                //Search on left;
                r=mid-1;

            } else {
                l=mid+1;
            }
        }
        return ans;
        
    }
};