class Solution {
public:
    int countPallindromeLength(string& s,int& l,int& r) {
        if(l<0 || r>=s.size()) return 0;
        while(l>=0 && r<s.size() && s[l]==s[r]) {
            l--;
            r++;
        }
        l++;
        r--;
        return r-l+1;
    }
    string longestPalindrome(string s) {
        //Approach - for each character i, find longest pallindrome substring with center char as i(both even and odd length)
        int maxLenLPointer=0;
        int maxLenRPointer=0;
        int l=0;
        int r=0;
        int count=0;
        int maxLengthPallindrome=0;
        int n = s.size();
        for(int i=0;i<n;i++) {
            //First consider even length pallindromes
            l=i;
            r=i+1;
            count=countPallindromeLength(s,l,r);
            if(count>maxLengthPallindrome) {
                maxLengthPallindrome = count;
                maxLenLPointer=l;
                maxLenRPointer=r; 
            }
            //Count odd length pallindromes
            l=i-1;
            r=i+1;
            count=countPallindromeLength(s,l,r);
            count=countPallindromeLength(s,l,r);
            if(count>maxLengthPallindrome) {
                maxLengthPallindrome = count;
                maxLenLPointer=l;
                maxLenRPointer=r; 
            }
        }
return s.substr(maxLenLPointer, maxLenRPointer - maxLenLPointer+1);
    }
};