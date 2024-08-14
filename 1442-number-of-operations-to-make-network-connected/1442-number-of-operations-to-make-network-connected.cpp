class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        vector<vector<int>> adjList(n);
        for(auto connection:connections) {
            adjList[connection[0]].push_back(connection[1]);
            adjList[connection[1]].push_back(connection[0]);
        }
        //Above will give us the graph
        //Now we need number of component components along with redundant wires
        int disconnectedComponents=0;
        int extraWires=0;
        //Go over all the systems
        vector<int> visited(n,0);
        for(int node=0;node<n;node++) {
            if(visited[node]==0) {
                disconnectedComponents++;
                //Do bfs
                queue<int> q;
                q.push(node);
                visited[node]=1;
                int totalWiresUsed=0;
                int nodesInComponent=0;
                while(!q.empty()) {
                    int n = q.front();
                    totalWiresUsed+=adjList[n].size();
                    nodesInComponent+=1;
                    q.pop();
                    for(auto neighbour:adjList[n]) {
                        if(visited[neighbour]==0) {
                            visited[neighbour]=1;
                            q.push(neighbour);
                        }
                    }
                }
                extraWires+=(totalWiresUsed/2)-(nodesInComponent-1);
            } 
        }
    if(disconnectedComponents-1<=extraWires) return (disconnectedComponents-1);
    return -1;
        
    }
};