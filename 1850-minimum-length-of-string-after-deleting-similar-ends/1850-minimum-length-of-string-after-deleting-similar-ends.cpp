class Solution {
public:
    int minimumLength(string s) {
        int l=0;
        int n = s.size();
        int r = s.size()-1;
        if(n==1) return 1;
        while(l<=r) {
            if(s[l]==s[r]){
                while(l<=r && s[l]==s[r]) {
                    l++;
                    r--;
                    if(l==r && s[l]!=s[l-1]) return 1;
                    if(l>=r) return 0;
                }
               
                while(l<n && l<r && s[l]==s[l-1]) l++;
                while(r>=0 && r>l&& s[r]==s[r+1]) r--;
            } else {
                break;
            }
        }
        
        return r-l+1;
        
    }

};