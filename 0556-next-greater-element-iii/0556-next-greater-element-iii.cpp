class Solution {
public:
    int nextGreaterElement(long long num) {
        if (num==INT_MAX) return -1;
        vector<int> arr;
        while(num!=0) {
            arr.push_back(num%10);
            num/=10;
        }
        reverse(arr.begin(),arr.end());
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
        } else { return -1; }
        reverse(arr.begin()+largestIndex+1,arr.end());
        string ans;
        for(auto a:arr) ans+=to_string(a);
        long long newans= stoll(ans);
        cout<<"newans is "<<newans<<endl;
        if(newans>INT_MAX) return -1;
        return newans;
    }
};