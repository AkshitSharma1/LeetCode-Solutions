class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
       int l=0;
       int n = arr.size();
       int r = n-1;
       int index=-1;
       int mid=0;
       while(l<=r) {
        mid = (l+r)/2;
        if(r-l==1) {
            if(arr[r]<arr[l]) return l;
            return r;
        }
        if (arr[mid]>arr[mid-1] && arr[mid]<arr[mid+1]) {
            //Rising edge of peak. ans will be on right
            l = mid+1;
        } else if(arr[mid]>arr[mid-1]&&arr[mid]>arr[mid+1]) {
             return mid;
        } else if(arr[mid]<arr[mid-1] && arr[mid]>arr[mid+1]) {
            //Falling edge of peak. answer lies on left
            r=mid-1;
        }
       }
        return mid;//useless but OK
    }
};