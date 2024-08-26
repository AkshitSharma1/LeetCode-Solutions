class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int,int> fruitCount;
        int i=0;
        int j=0;
        int distinctCount=0;
        int ans=0;
        while(j<fruits.size()) {
            fruitCount[fruits[j++]]++;
            if(fruitCount[fruits[j-1]]==1) { distinctCount++;}
            if(distinctCount>2) {
                while(distinctCount>2) {
                    fruitCount[fruits[i++]]--;
                    if(fruitCount[fruits[i-1]]==0) distinctCount-=1;
                }
            }
            ans = max(ans,j-i);



        }
        return ans;
    }
};