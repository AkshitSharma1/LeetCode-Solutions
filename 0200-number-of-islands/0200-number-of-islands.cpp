class Solution {
public:
    void dfs(int r,int c,int m,int n, vector<vector<int>>& visited,vector<vector<char>>& grid) {
        vector<pair<int,int>> disp = {{-1,0},{1,0},{0,1},{0,-1}};
        visited[r][c]=1;
        for(auto d:disp) {
            int r_new = r+d.first;
            int c_new = c+d.second;
            if(r_new>=0 && r_new<m && c_new>=0 && c_new<n) {
                if(grid[r_new][c_new]=='1' && visited[r_new][c_new]==0) {
                    dfs(r_new,c_new,m,n,visited,grid);
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> visited(m,vector<int>(n,0));
        int distinctIslands=0;
        for(int r=0;r<m;r++) {
            for(int c=0;c<n;c++) {
                if(grid[r][c]=='1' && visited[r][c]==0) {
                    dfs(r,c,m,n,visited,grid);
                    distinctIslands++;
                }
            }
        }
        return distinctIslands;
        
    }
};