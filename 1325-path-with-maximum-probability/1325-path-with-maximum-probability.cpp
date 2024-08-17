class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        priority_queue<pair<double,int>> pq;
        vector<vector<pair<int,double>>> adjList(n);
        int edgeNumber=0;
        for(auto edge:edges) {
            adjList[edge[0]].push_back({edge[1],succProb[edgeNumber]});
            adjList[edge[1]].push_back({edge[0],succProb[edgeNumber]});

            edgeNumber++;
        }
        vector<double> dist(n,-1);
        dist[start_node]=-1;
        pq.push({1,start_node});
        while(!pq.empty()) {
            auto top = pq.top();
            pq.pop();
            for(auto node:adjList[top.second]) {
                double edgeProb = node.second;
                int neighbour = node.first;
                if(neighbour==start_node) continue;
              
                if(dist[neighbour]<top.first*edgeProb) {
                    dist[neighbour] = top.first*edgeProb;
                    pq.push({dist[neighbour],neighbour});
                }
            }
        }
        return dist[end_node]==-1?0:dist[end_node];
        
    }
};