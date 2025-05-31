class Solution {
public:
    
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int N(mat.size()),M(mat[0].size());
        vector<vector<int>> dist(N,vector<int>(M,1e7));
        vector<vector<int>> visited(N,vector<int>(M,0));
        queue<pair<int,int>> q;
        for(int i=0;i<N;i++) {
            for(int j=0;j<M;j++) {
                if(mat[i][j]==0) {
                    dist[i][j]=0;
                    visited[i][j]=1;
                    q.push({i,j});
                }
            }
        }
        while(!q.empty()) {
            auto temp = q.front();
            q.pop();
            int r = temp.first;
            int c = temp.second;
            vector<pair<int,int>> dirs = {{r+1,c},{r-1,c},{r,c+1},{r,c-1}};
            for(auto dir:dirs) {
                //Check if its valid
                int rn(dir.first),cn(dir.second);
                if(rn<0 or rn>=N or cn<0 or cn>=M) continue;
                if(visited[rn][cn]==0) {
                    visited[rn][cn]=1;
                    dist[rn][cn]=dist[r][c]+1;
                    q.push({rn,cn});
                }
            }
        }
        return dist;
    }
};