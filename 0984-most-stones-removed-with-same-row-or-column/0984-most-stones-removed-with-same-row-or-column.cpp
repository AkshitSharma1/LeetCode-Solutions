class Solution {
public:
    void dfs(int i,unordered_map<int,vector<int>>& adjList,unordered_set<int>& visited) {
        visited.insert(i);
        for(auto neighbour:adjList[i]) {
            if(visited.find(neighbour)==visited.end()) {
                dfs(neighbour,adjList,visited);
            }
        }
    }
    int removeStones(vector<vector<int>>& stones) {
        //Answer (because of visualization) will be = number of connected components
        int n = stones.size();
        unordered_map<int,vector<int>> adjList;
        unordered_set<int> visited;
        for(int i=0;i<n;i++) {
            for(int j=i+1;j<n;j++) {
                if(stones[j][0]==stones[i][0] || stones[j][1]==stones[i][1]) {
                    adjList[i].push_back(j);
                    adjList[j].push_back(i);
                }

            }
        }
        //For each node, call DFS
        int connectedComponents=0;
        for(int i=0;i<n;i++) {
            if(visited.find(i)==visited.end()) {
                connectedComponents++;
                dfs(i,adjList,visited);
            }
        }
        return n - connectedComponents;
        
    }
};