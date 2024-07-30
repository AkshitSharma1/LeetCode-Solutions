class Solution {
public:
    int countBinarySubstrings(string s) {
        int l=0;
        int r=0;
        int n = s.length();
        unordered_map<int,int> mp;
        int oneCount=0;
        int zeroCount=0;
        int diff=0;
        int ans=0;
        mp[0]=1;
        while(r<n) {
            if(r>0 && s[r]=='0' && s[r]!=s[r-1]&&zeroCount>0) {
                while(l<r && s[l]=='0') {
                   zeroCount-=1;
                    l+=1;
                }
                mp.clear();
                mp[0]=1;
                for(int i=1;i<=oneCount;i++) {
                    mp[i]=1;
                }
                continue;
            }



 if(r>0 && s[r]=='1' && s[r]!=s[r-1]&&oneCount>0) {
                while(l<r && s[l]=='1') {
                   oneCount-=1;
                    l+=1;
                }
                mp.clear();
                mp[0]=1;
                for(int i=1;i<=zeroCount;i++) {
                    mp[(-1)*i]=1;
                }
                continue;
            }



            if(s[r]=='0') {zeroCount++;} else { oneCount++;}
            diff = oneCount-zeroCount;
            if(mp.find(diff)!=mp.end()) ans+=mp[diff];
            mp[diff]++;
            r++;
        }
        return ans;
    }

};