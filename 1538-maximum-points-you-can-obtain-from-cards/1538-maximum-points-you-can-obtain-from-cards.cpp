class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        // This is equivalent to finding sliding window of n-k size such that sum of elements is minimum
        int n = cardPoints.size();
        int winSize = n-k;
        
        int i=0;
        int j=0;
        long long minSum=INT_MAX;
        long long totalSum =0;
        for(auto cardPoint:cardPoints) totalSum+=cardPoint;
      
        long long sum=0;
        //Grow phase
        while(j<winSize-1) {
            sum+=cardPoints[j];
            j=j+1;
        }
       

        while(j<n && j-i+1==winSize) {
            //Process the window
            sum+=cardPoints[j];
           // cout<<sum<<endl;
            minSum = min(sum,minSum);

            //Prepare to move the window
            sum-=cardPoints[i];

            //Move the window
            i++;
            j++;
        }

        return (minSum==INT_MAX)?totalSum: totalSum-minSum;

        
    }
};