class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int ans=0;
        int l=0;
        int r = people.size()-1;
        int sum=0;
        while(l<=r) {
            if(l==r) {
                ans+=1;
                break;
            }
            sum = people[l]+people[r];
            if(sum>limit) {
                r-=1;
                ans+=1; //Send the heavier one on separate boat
            } else if(sum<=limit) {
                r-=1;
                l+=1;
                ans+=1; //1 Boat for both
            }
        }
            return ans;

        }
};