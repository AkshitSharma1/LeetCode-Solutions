class Solution {
public:
    int hIndex(vector<int>& citations) {
        int l=0;
        int n = citations.size();
        int r = citations[n-1];
        int mid=0;
        int possibleAns=0;
        while(l<=r) {
            int validCiteCount=0;

            mid = (l+r)/2;
            for(auto citation:citations) {
                if (citation>=mid) {validCiteCount+=1;}
            }
            if (validCiteCount>=mid) {
                //Can we have even a bigger h index?
                possibleAns=mid;
                //Try searching right?
                l = mid+1;
            } else {
                r = mid-1;
            }

        }
            

        
        return possibleAns;

        
    }
};