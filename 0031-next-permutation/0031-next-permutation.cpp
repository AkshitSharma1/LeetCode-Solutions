class Solution {
public:
    void nextPermutation(vector<int>& arr) {
        int n = arr.size();
        int largestIndex=-1;

        for(int i=0;i<n-1;i++) {
            if(arr[i]<arr[i+1]) {
                largestIndex=i;
            }
        }
        if (largestIndex!=-1) {
        for(int j=n-1;j>=largestIndex+1;j--) {
            if(arr[j]>arr[largestIndex]) {
                swap(arr[j],arr[largestIndex]);
                break;
            }
        }
        }
        reverse(arr.begin()+largestIndex+1,arr.end());
    }
};