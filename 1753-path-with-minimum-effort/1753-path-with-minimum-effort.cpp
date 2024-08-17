class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> dist(m,vector<int>(n,1e7));
        dist[0][0]=0;
        priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,greater<pair<int,pair<int,int>>>> pq;
        vector<pair<int,int>> displacement = {{1,0},{-1,0},{0,1},{0,-1}};
        pq.push({0,{0,0}});
        while(!pq.empty()) {
            auto top = pq.top();
            pq.pop();
            int y = top.second.first;
            int x = top.second.second;
            int  minCostSoFar = top.first;
            for(auto disp:displacement) {
                int new_x =x+disp.second;
                int new_y = y+disp.first;
                if(new_y<m&&new_y>=0 && new_x>=0 && new_x<n) {
                    if(max(minCostSoFar,abs(heights[new_y][new_x]-heights[y][x]))<dist[new_y][new_x]) {
                        dist[new_y][new_x] = max(minCostSoFar,abs(heights[new_y][new_x]-heights[y][x]));
                        pq.push({dist[new_y][new_x],{new_y,new_x}});
                    }
                }
            }
            
        }
        return dist[m-1][n-1];
    }
};