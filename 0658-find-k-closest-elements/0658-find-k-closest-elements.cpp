class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int indexOfX=0;
        int minDiff=INT_MAX;
        int minIndex=0;
        int minElement=INT_MAX;
        int i=0;
        vector<int> ans;
        for(auto num:arr) {
            if(abs(num-x)<minDiff || (abs(num-x)==minDiff && num<minElement)) {
                minIndex=i;
                minElement=num;
                minDiff = abs(num-x);
            } 
            i+=1;
        }
        cout<<"closest element: "<<minElement<<" with index "<<minIndex<<endl;
        int count=0;
        int n=arr.size();
        ans.push_back(arr[minIndex]);
        count+=1;
        if(count==k) return ans;
        int lPointer=minIndex-1;
        int rPointer=minIndex+1;
        while(lPointer>=0 && rPointer<n) {
            if(abs(arr[lPointer]-x)<abs(arr[rPointer]-x) ||
             (abs(arr[lPointer]-x)==abs(arr[rPointer]-x) && arr[lPointer]<arr[rPointer])) {
                ans.push_back(arr[lPointer]);
                count+=1;
                lPointer-=1;

            } else {
                ans.push_back(arr[rPointer]);
                rPointer+=1;
                count+=1;
            }
            if(count==k) break;
        }
        if(count==k) {
            sort(ans.begin(),ans.end());
            return ans;
        }
        if(count<k && lPointer<0) {
            while(rPointer<n && count<k) {
                ans.push_back(arr[rPointer]);
                rPointer+=1;
                count+=1;
            }
        } else if(count<k && rPointer==n) {
            while(lPointer>=0 && count<k) {
                ans.push_back(arr[lPointer]);
                lPointer-=1;
                count+=1;
            }
        }
                    sort(ans.begin(),ans.end());

        return ans;
        
    }
};