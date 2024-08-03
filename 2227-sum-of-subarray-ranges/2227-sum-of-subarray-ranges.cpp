class Solution {
public:
    long long subArrayRanges(vector<int>& arr) {
          long long MOD = 1e9+7;
        stack<pair<int,int>> st1; //Next smaller element on right
        int n = arr.size();
        vector<long long> smallerOnLeft(n,-1);
       vector<long long> smallerOnRight(n,n);
          vector<long long> greaterOnLeft(n,-1);
       vector<long long> greaterOnRight(n,n);


        stack<pair<int,int>> st2;//Next smaller element on left
                stack<pair<int,int>> st3;//Next greater element on left
        stack<pair<int,int>> st4;//Next greater element on right

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




           for(int i=0;i<n;i++) {
          if(st3.empty()) {
            st3.push({arr[i],i});
          } else {
            while(st3.empty()==false && st3.top().first<=arr[i]) {
                st3.pop();
            }
            if(!st3.empty()) {
                greaterOnLeft[i]=st3.top().second;
            }
            st3.push({arr[i],i});
          } 
        }


         for(int i=n-1;i>=0;i--) {
          if(st4.empty()) {
            st4.push({arr[i],i});
          } else {
            while(st4.empty()==false && st4.top().first<arr[i]) {
                st4.pop();
            }
            if(!st4.empty()) {
                greaterOnRight[i]=st4.top().second;
            }
            st4.push({arr[i],i});
          } 
        }
                long long ans=0;


        for(int i=0;i<n;i++) {
            long long diff1=(greaterOnRight[i]-i)*(i-greaterOnLeft[i]);
            long long diff2 = (smallerOnRight[i]-i)*(i-smallerOnLeft[i]);
            long long finalDiff = diff1-diff2;
            ans+=finalDiff*arr[i];
        }




return ans;
    }
};