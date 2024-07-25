class Solution {
public:
    int findBestValue(vector<int>& arr, int target) {
        //Search space is linear (O(N))
        //Max value = Max element in array
        sort(arr.begin(),arr.end());
        int l=0;
        int r=arr[arr.size()-1];
        int mid = (l+r)/2;
        int minDiff=INT_MAX;
        int ans=INT_MAX;
        while (l<=r) {
            int sum=0;
            //Calculate sum & min diff
            for(auto num:arr) {
                if (num<=mid) {
                    sum+=num;
                } else { sum+=mid; }
            }
            int diff=abs(sum-target);
             

            if (diff<=minDiff) {
                if(diff<minDiff) ans = mid;
                if(diff==minDiff && mid<ans) ans=mid;

                minDiff = diff;
            }
            if(sum>=target) {
                //Make sum smaller by moving to the left
                r = mid -1;
            } else if(sum<target) {
                //Make sum larger by moving to the right;
                l = mid+1;
            } 
            mid = (l+r)/2;

            
        }
        return ans;
    }

};