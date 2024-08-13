class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        queue<pair<int,int>> q;
        int m = image.size();

        int n = image[0].size();
        q.push({sr,sc});
        vector<vector<int>> visited(m,vector<int>(n,0));
        visited[sr][sc]=1;
        int originalColor = image[sr][sc];
        vector<pair<int,int>> displacement = {{-1,0},{1,0},{0,1},{0,-1}};
        while(!q.empty()) {
            auto top = q.front();
            int y = top.first;
            int x = top.second;
            q.pop();
            image[y][x]=color;
            for(auto disp:displacement) {
                int dy = disp.first;
                int dx = disp.second;

                if(x+dx>=0 && x+dx<n && y+dy>=0 && y+dy<m) {
                    if(image[y+dy][x+dx]==originalColor && visited[y+dy][x+dx]==0) {
                        visited[y+dy][x+dx]=1;
                        q.push({y+dy,x+dx});
                    }
                }
            }

        }
        return image;
    }
};