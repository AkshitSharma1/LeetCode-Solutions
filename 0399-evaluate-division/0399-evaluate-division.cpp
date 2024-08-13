class Solution {
public:



    double dfs(int currNode,int targetNode,int parentNode,vector<int>& visited,vector<vector<pair<int,double>>>& adjList,double ans) {

        if (currNode==targetNode) return ans;
        visited[currNode]=1;
        for(auto neighbour:adjList[currNode]) {
            if(visited[neighbour.first]==1 && neighbour.first!=parentNode) return -1; //base case
            if(visited[neighbour.first]!=1) {
                double response = dfs(neighbour.first,targetNode,currNode,visited,adjList,ans*neighbour.second);
                if(response!=-1) return response;
            }
        }
        return -1;
    }
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string,int> mp;
        int v=0;
        for(auto equation:equations) {
            if(mp.find(equation[0])==mp.end()) {
                mp[equation[0]]=v;
                v++;
            }   

              if(mp.find(equation[1])==mp.end()) {
                mp[equation[1]]=v;
                v++;
            }   
    }
    //Create adjancency list with weights
    vector<vector<pair<int,double>>> adjList(v+1);
    for(int i=0;i<equations.size();i++) {
        adjList[mp[equations[i][0]]].push_back({mp[equations[i][1]],values[i]});
        adjList[mp[equations[i][1]]].push_back({mp[equations[i][0]],(double)1/values[i]});
    }

    //Now apply dfs. if cycle exists or the node doesnt exist in mp return -1
    vector<double> answer;
    for(auto query:queries) {
        if(mp.find(query[0])==mp.end()||mp.find(query[1])==mp.end()) {
            answer.push_back(-1);
            continue;
        } 

        //Perform the computation
        int startNode=mp[query[0]];
        int targetNode = mp[query[1]];
        vector<int> visited(v+1,-1);
        answer.push_back(dfs(startNode,targetNode,-1,visited,adjList,1));
    }
    return answer;
    }
};