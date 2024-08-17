class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
        //{min_dist,min_node}
        vector<vector<pair<int,int>>> adjList(n+1);
        for(auto time:times) {
            adjList[time[0]].push_back({time[1],time[2]});
        }


        unordered_map<int,int> dist;
        for(int i=1;i<=n;i++) dist[i]=1e5;
        dist[k]=0;
        pq.push({0,k});
        while(!pq.empty()) {
            pair<int,int> top = pq.top();
            pq.pop();
            for(auto node:adjList[top.second]) {
                int neighbour = node.first;
                int wt = node.second;
                if(dist[top.second]+wt<dist[neighbour]) {
                    dist[neighbour] = dist[top.second]+wt;
                    pq.push({dist[neighbour],neighbour});
                }
            }
        }
        int maxDist = 0;
        for(auto d:dist) {
            maxDist = max(maxDist,d.second);
        }
        if (maxDist==1e5) return -1;
        return maxDist;
        

    }
};