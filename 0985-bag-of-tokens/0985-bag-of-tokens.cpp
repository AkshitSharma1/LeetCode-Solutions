class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int l=0;
        int n = tokens.size();
        int r =n-1;
        int score=0;
        sort(tokens.begin(),tokens.end());
        while(l<=r) {
            while(l<=r && tokens[l]<=power) {
             power-=tokens[l];
             score+=1;
             l+=1;
            } 
             if(l<r && tokens[l]>power) {
                if(score>0) {
                    power+=tokens[r];
                    r-=1;
                    score-=1;
                } else {break; }
            } else if(l==r && tokens[l]>power) break;
        }
        return score;
        
    }
};