class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        //Two-pass linear sweep O(nlgn+mlgm)
        int i=0;
        int j=0;
        sort(arr1.begin(),arr1.end());
        sort(arr2.begin(),arr2.end());
        //We need distance from both the ends -> Forward pass and backward pass
        int n = arr1.size();
        int m = arr2.size();
        //We will store min dist for each element in arr1 wrt arr2
        vector<int> forwardPass(n,INT_MAX);
        vector<int> backwardPass(n,INT_MAX);
        while(i<n && j<m) {
            //O(n+m)
            if(arr1[i]<=arr2[j]) {
                forwardPass[i] = abs(arr2[j]-arr1[i]);
                i++;
            } else {
                j++;
            }
        }

        //Now backward pass
        i=n-1;
        j=m-1;
        while(i>=0 && j>=0) {
            if(arr2[j]<=arr1[i]) {
                backwardPass[i] = min(backwardPass[i],abs(arr2[j]-arr1[i]));
                i--;
            } else { j--;}
        }
        //Now, we have min dist for each forward and backward pass
        int ans=0;
        for(int i=0;i<n;i++) {
            if(min(backwardPass[i],forwardPass[i])>d) ans++;
        }
        return ans;

    }
};