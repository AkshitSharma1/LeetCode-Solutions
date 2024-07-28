class Solution {
public:
    bool checkPallindrome(string &s, int l,int r) {
        while(l<r) {
            if(s[l]!=s[r]) return false;
            l++;
            r--;

        }
        return true;
    }
    bool validPalindrome(string s) {
        int l=0;
        int n = s.size();
        int r = n-1;
        while(l<r) {
            if(s[l]==s[r]) {
                l++;
                r--;
            } else {
                return checkPallindrome(s,l+1,r) || checkPallindrome(s,l,r-1);
            }

        }
        return true;
        
    }
};