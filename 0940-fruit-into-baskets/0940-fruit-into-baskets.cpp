class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int i=0;
        int j=0;
        int n = fruits.size();
        int ans=0;
        unordered_map<int,int> mp;
        int distinct_count=0; 
        while(j<n) {
            //Process this
            mp[fruits[j]]+=1;
            if(mp[fruits[j]]==1) distinct_count+=1;
            
            while(distinct_count>2) {
                //While win size is more than 2 , we will keep on decreasing win size
                mp[fruits[i]]--;
                if(mp[fruits[i]]==0) distinct_count-=1;
                i++;
            }

            if(distinct_count<=2) ans = max(ans,j-i+1);
            j++;
            
        }
            return ans;

    }
};