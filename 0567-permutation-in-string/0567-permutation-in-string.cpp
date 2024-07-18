class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int i=0;
        int j=0;
        unordered_map<char,int> mp;
        for(auto x:s1) mp[x]+=1;
        int distinct_count = mp.size();
        int k = s1.length();
        int n = s2.length();
        
        //Is the window size>n?
        if(k>n) return false;
        //Grow the window
        while(j<k-1) {
            if( mp.find(s2[j])!=mp.end()) {
                //It exists
                mp[s2[j]]-=1;
                if(mp[s2[j]]==0) distinct_count-=1;
            }
            j++;
        }

        while(j<n) {
            //Process the window
            if(mp.find(s2[j])!=mp.end()) {
                mp[s2[j]]-=1;
                if(mp[s2[j]]==0) distinct_count-=1;
            }
            if(distinct_count==0) {return true;}
            //Prepare to move the window
            if(mp.find(s2[i])!=mp.end()) {
                mp[s2[i]]+=1;
                if(mp[s2[i]]==1) distinct_count+=1;
            }

            //Move the window
            i++;
             j++; 
        }

        return false;    
    }
};
