class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        //Monotonic stack (both increasing from left->right and right->left) for smallest element index
        stack<pair<int,int>> stackLeftToRight; 
        stack<pair<int,int>> stackRightToLeft; 
        int n = heights.size();
        vector<int> smallerElementIndexOnLeft(n,-1);
        vector<int> smallerElementIndexOnRight(n,n);
        for(int i=0;i<n;i++) {
            if(stackLeftToRight.empty()) {
                stackLeftToRight.push({heights[i],i});
            } else {
                while(stackLeftToRight.empty()==false && stackLeftToRight.top().first>=heights[i]) {
                    stackLeftToRight.pop();
                }
                if(stackLeftToRight.empty()) {
                    stackLeftToRight.push({heights[i],i});
                } else {
                    smallerElementIndexOnLeft[i]=stackLeftToRight.top().second;
                    stackLeftToRight.push({heights[i],i});


                }
            }
        }

        for(int i=n-1;i>=0;i--) {
            if(stackRightToLeft.empty()) {
                stackRightToLeft.push({heights[i],i});
            } else {
                while(stackRightToLeft.empty()==false && stackRightToLeft.top().first>=heights[i]) {
                    stackRightToLeft.pop();
                } 
               if(stackRightToLeft.empty()) {
                    stackRightToLeft.push({heights[i],i});
                } else {
                    smallerElementIndexOnRight[i]=stackRightToLeft.top().second;
                    stackRightToLeft.push({heights[i],i});


                }
            }
        }

    int ans=INT_MIN;
    for(int i=0;i<n;i++) {
    ans = max(ans,(smallerElementIndexOnRight[i]-smallerElementIndexOnLeft[i]-1)*heights[i]);   
        }
        return ans;
    }
};