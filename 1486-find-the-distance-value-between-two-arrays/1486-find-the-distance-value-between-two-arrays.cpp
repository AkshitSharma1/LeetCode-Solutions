class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int n = arr1.size();
        int m = arr2.size();
        //We will calculate distance value for each a1 in arr1
        vector<int> forwardDist(n,INT_MAX);
        vector<int> backwardDist(n,INT_MAX);
        sort(arr1.begin(),arr1.end());
        sort(arr2.begin(),arr2.end());
        int i=0;
        int j=0;
        while(i<n&&j<m) {
            if(arr2[j]>=arr1[i]) {
                forwardDist[i] = min(forwardDist[i],arr2[j]-arr1[i]);
                i++;
            } else {
                j++;
            }
        }
        i=n-1;
        j=m-1;
        while(i>=0 && j>=0) {
            if(arr1[i]>=arr2[j]) {
                backwardDist[i] = min(backwardDist[i],arr1[i]-arr2[j]);
                i--;
            } else { j--;}
        }
        int count=0;
        for(int i=0;i<n;i++) {
            if (min(abs(forwardDist[i]),abs(backwardDist[i]))>d) count++;
        }
        return count;
    }
};