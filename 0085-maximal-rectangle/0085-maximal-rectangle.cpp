class Solution {
public:
    int returnMaxArea(vector<int>& heights) {


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

    
    
    
    int maximalRectangle(vector<vector<char>>& matrix) {
        vector<vector<int>> heights(matrix.size(),vector<int>(matrix[0].size(),0));
        for(int i=0;i<matrix[0].size();i++) {
            if(matrix[0][i]=='1') heights[0][i]=1;
        }
        int ans=0;

        for(int r=1;r<matrix.size();r++) {
            for(int c=0;c<matrix[0].size();c++) {
                if (matrix[r][c]=='1') {

                 heights[r][c]=1+heights[r-1][c];
            } else {
                heights[r][c] = 0 ;
            }
        }

        }

        cout<<"height matrix is "<<endl;
        for(auto row:heights) {
            for(auto col:row) cout<<col<<" ";
            cout<<endl;
        }


        for(int i=0;i<matrix.size();i++) ans=max(ans,returnMaxArea(heights[i]));
return ans;
    }

};