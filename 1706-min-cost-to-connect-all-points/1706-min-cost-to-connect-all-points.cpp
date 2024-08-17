class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        //Prims algorithm
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
        unordered_set<int> visited;
        unordered_map<int,vector<pair<int,int>>> adjList;
        int n = points.size();
        for(int i=0;i<n;i++) {
            for(int j=i+1;j<n;j++) {
                adjList[i].push_back({j,abs(points[j][1]-points[i][1])+abs(points[i][0]-points[j][0])});
                adjList[j].push_back({i,abs(points[j][1]-points[i][1])+abs(points[i][0]-points[j][0])});

            }
        }
        pq.push({0,0});
        int ans=0;
        while(!pq.empty()) {
            auto top = pq.top();
            int node = top.second;
            int wt = top.first;
            pq.pop();
            if(visited.find(node)!=visited.end()) continue;
            visited.insert(node);
            ans+=wt;
            for(auto neighbour:adjList[node]) {
                if (visited.find(neighbour.first)==visited.end()) {

                    pq.push({neighbour.second,neighbour.first});
                }
            }
        }
        return ans;

    }
};