class Solution {
public:
    void reverseString(vector<char>& s) {
        int l=0;
        int r = s.size()-1;
        char c;
        while(l<=r) {
            c=s[l];
            s[l]=s[r];
            s[r]=c;
            l+=1;
            r-=1;
        }
    }
};