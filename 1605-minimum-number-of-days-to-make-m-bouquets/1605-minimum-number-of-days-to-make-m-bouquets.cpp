class Solution {
public:

    bool isValid(int m,int k,int mid,vector<int>& bloomDay) {
        //Check for m continuous subgroups of k adj flowers
        int tempCount=0;
        int ans=0;
        for (auto bloomday:bloomDay) {
            if(bloomday<=mid) {
                tempCount+=1;
            } else {
                tempCount=0;
            }
            if(tempCount==k) {
                ans+=1;
                tempCount=0;
            }
        }
        if(ans>=m) return true;
        return false;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        //Binary search 
        //First find the minimum day and max day
        int minBloomDay = INT_MAX;
        int maxBloomDay = INT_MIN;
        for(auto bloomday:bloomDay) {
            minBloomDay = min(bloomday,minBloomDay);
            maxBloomDay = max(bloomday,maxBloomDay);
        }

        int l = minBloomDay;
        int r = maxBloomDay;

        int mid = l+(r-l)/2;
        int ans=-1;
        while (l<=r) {
            //Is it possible to m banuquets of k adj flowers with mid days
            if (isValid(m,k,mid,bloomDay)) {
                ans=mid;
                //Can we go even less?
                r = mid-1;
            } else {
                l = mid+1;
            }
            mid  = l+(r-l)/2;
        }
        return ans;



    }
};