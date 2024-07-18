class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        int i=0;
        int j=0;
        unordered_map<char,int> mp;
        int n = s.length();
        int adj_pair=0;
        int ans=0;
        while(j<n) {
            //Process the current window
            mp[s[j]]++;
            if(j-i+1>1) {
                //Window size is more than one, check if the prev char and this are same or not
                if(s[j]==s[j-1]) adj_pair+=1;
            }

            //If we did a mistake - correct the mistake
            while (adj_pair>1) {
                mp[s[i]]--;
                if(j-i+1>1) {
                    if(s[i+1]==s[i]) adj_pair-=1;
                }
                i++;
            }
            if(adj_pair<=1) {
                ans  = max(ans,j-i+1);
            }
            j=j+1;

        }
        return ans;
    }
};