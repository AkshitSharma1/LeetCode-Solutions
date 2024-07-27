class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        long long count=0;
        sort(arr.begin(),arr.end());
        long long MOD = 1e9+7;
        long long sum=0;
        unordered_map< long long, long long> mp;
        for(auto num:arr) mp[num]+=1;
        long long ans=0;
        for(int start=0;start<arr.size();start++) {
            mp[arr[start]]-=1;
            int l=start+1;
            int r = arr.size()-1;
            while(l<r) {
                if(l>=arr.size()) break;
                sum = arr[start]+arr[l]+arr[r];
                if(sum>target) {
                    //Try decreasing the sum
                    r-=1;
                } else if(sum<target) {
                    l+=1;
                } else{
                    if(arr[l]==arr[r]) {
                        ans+=(mp[arr[l]]*(mp[arr[l]]-1)/2)%MOD;
                        
                    } else {
                    ans+=(mp[arr[l]]*mp[arr[r]])%MOD;
                    }
                    ans%=MOD;
                    l+=1;
                    r-=1;
                    while(l<arr.size()&&arr[l]==arr[l-1]) l+=1;
                    while(r>=0&&arr[r]==arr[r+1]) r-=1;

                }

            }

        }
                   return ans;
 
    }
};