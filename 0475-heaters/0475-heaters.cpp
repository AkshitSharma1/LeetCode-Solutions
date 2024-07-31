class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
     sort(houses.begin(),houses.end());
     sort(heaters.begin(),heaters.end());
     int i=0;
     int j=0;
     int n = houses.size();
     int m = heaters.size();
     vector<int> forwardDist(n,INT_MAX);   
    vector<int> backwardDist(n,INT_MAX);
    while(i<n&&j<m) {
        if(houses[i]<=heaters[j]) {
            forwardDist[i]=min(forwardDist[i],heaters[j]-houses[i]);
            i++;
        } else {
            j++;
        }
    }
     i=n-1;
     j=m-1;
    while(i>=0 && j>=0) {
        if(heaters[j]<=houses[i]) {
            backwardDist[i] = min(backwardDist[i],-heaters[j]+houses[i]);
            i-=1;
        } else {
            j-=1;

        }
    }
    int ans=0;
    for(int i=0;i<n;i++) {
        ans = max(min(backwardDist[i],forwardDist[i]),ans);
    }
    return ans;
  

    }
};