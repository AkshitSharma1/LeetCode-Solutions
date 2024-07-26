class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l=0;
        int n = letters.size();
        int r = n-1;
        int mid=0;
        char ans=letters[0];
        int mindiff=INT_MAX;
        while(l<=r) {
            mid = (l+r)/2;
            if (target>=letters[mid]) {
                l = mid+1;
            } else if(target<letters[mid]) {
                int diff = letters[mid]-target;
                if(diff<mindiff) {
                    mindiff=diff;
                    ans=letters[mid];
                }
                r = mid-1;
            }
        }
        return ans;
    }
};