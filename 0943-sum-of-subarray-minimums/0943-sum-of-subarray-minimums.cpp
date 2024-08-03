class Solution {
public:

    int sumSubarrayMins(vector<int>& arr) {
        long long MOD = 1e9+7;
        stack<pair<int,int>> st1; //Next smaller element on right
        int n = arr.size();
        vector<long long> smallerOnLeft(n,-1);
       vector<long long> smallerOnRight(n,n);

        stack<pair<int,int>> st2;//Next smaller element on left
        for(int i=0;i<n;i++) {
          if(st2.empty()) {
            st2.push({arr[i],i});
          } else {
            while(st2.empty()==false && st2.top().first>=arr[i]) {
                st2.pop();
            }
            if(!st2.empty()) {
                smallerOnLeft[i]=st2.top().second;
            }
            st2.push({arr[i],i});
          } 
        }


         for(int i=n-1;i>=0;i--) {
          if(st1.empty()) {
            st1.push({arr[i],i});
          } else {
            while(st1.empty()==false && st1.top().first>arr[i]) {
                st1.pop();
            }
            if(!st1.empty()) {
                smallerOnRight[i]=st1.top().second;
            }
            st1.push({arr[i],i});
          } 
        }

        long long ans=0;
        for(auto c:smallerOnLeft) cout<<c<<" ";
        cout<<endl;
        for(auto c:smallerOnRight) cout<<c<<" ";
        
        for(int i=0;i<n;i++) {
            ans+=((smallerOnRight[i]-i)*(i-smallerOnLeft[i])%MOD)*((long long)arr[i]%MOD);
        ans%=MOD;
        }

        return ans;
        
        
    }
};