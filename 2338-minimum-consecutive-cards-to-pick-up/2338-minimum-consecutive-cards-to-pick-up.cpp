class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        int i=0;
        int j=0;
        int n = cards.size();
        int ans=INT_MAX;
        int pair_count=0;
        unordered_map<int,int> mp;
        for(auto card:cards) mp[card]=0;
        while(j<n) {
            //Process current window
            pair_count+=mp[cards[j]];
            mp[cards[j]]+=1;

            //We want minimum pair_count
            while(pair_count>1) {
                //Shrink the window (i++)
                mp[cards[i]]--;
                pair_count-=mp[cards[i]];

                i++;
            }
            

            if(pair_count==1) {
                while(pair_count==1) {
                ans = min(ans,j-i+1);
                 mp[cards[i]]--;
                pair_count-=mp[cards[i]];
                i=i+1;
                }
            }
            j++;

        }
        return ans==INT_MAX?-1:ans;
    }
};