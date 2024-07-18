class Solution {
public:
    int countGoodSubstrings(string s) {
        int i=0;
        int j=0;
        unordered_map<char,int> mp;
        int ans=0;
        int n = s.length();
        int k = 3;
        int not_distinct_count=0;
        while(j<k-1) {
            mp[s[j]]+=1;
            if(mp[s[j]]==2) not_distinct_count+=1;
            j++;
        }
        while(j<n) {
        
            //Process the window
            mp[s[j]]+=1;
            if(mp[s[j]]==2) not_distinct_count+=1;

            if(not_distinct_count==0) ans++;

            //Prepare to move window phase
            mp[s[i]]-=1;
            if(mp[s[i]]==1) not_distinct_count-=1;

            i++;
            j++;


        }
        
        return ans;
    }
};