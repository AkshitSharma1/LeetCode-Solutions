class Solution {
public:
    bool minDistLessThanEqualD(vector<int>& arr2,int low,int high,int target,int dist) {
        int mid;
        while(low<=high) {
            mid = (low+high)/2;
            if (abs(arr2[mid]-target)<=dist) {
                 return true;
            } else if(arr2[mid]<target) {
                low=mid+1;
            } else {
                high = mid-1;
            }
        }
        return false;
    }
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        //Binary search
        int ans=0;
        int m = arr2.size();
        sort(arr1.begin(),arr1.end());
        sort(arr2.begin(),arr2.end());
        for(auto num:arr1) {
            if (minDistLessThanEqualD(arr2,0,m-1,num,d)==false) ans++;
        }
        return ans;

    }
};