class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        int i=0;
        int j=0;
        unordered_map<char,int> mp;
        for(auto x:p) mp[x]+=1;
        int distinct_count = mp.size();
        int k = p.length();
        int n = s.size();
        //Grow the window
        while(j<k-1) {
            if( mp.find(s[j])!=mp.end()) {
                //It exists
                mp[s[j]]-=1;
                if(mp[s[j]]==0) distinct_count-=1;
            }
            j++;
        }


        while(j<n) {
            //Process the window
            if(mp.find(s[j])!=mp.end()) {
                mp[s[j]]-=1;
                if(mp[s[j]]==0) distinct_count-=1;
            }
            if(distinct_count==0) ans.push_back(i);
            //Prepare to move the window
            if(mp.find(s[i])!=mp.end()) {
                mp[s[i]]+=1;
                if(mp[s[i]]==1) distinct_count+=1;
            }

            //Move the window
            i++;
            j++;
        }


    return ans;    
    }
    
};