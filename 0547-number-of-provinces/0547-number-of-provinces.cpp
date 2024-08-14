class Solution {
public:

    bool dfs(vector<vector<int>>& isConnected,int node,vector<int>& visited) {

        if(visited[node]==true) return true;
        
        visited[node]=true;
            for(int x=0;x<isConnected[node].size();x++ ) {
                if(isConnected[node][x] && visited[x]==false) {
                    dfs(isConnected,x,visited);
                }
           
        } 
        return false;
        
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
      vector<int> visited(isConnected.size(),0);
      int nProvince=0;
      for(int i=0;i<isConnected.size();i++) {
          if(visited[i]==0) {
              dfs(isConnected,i,visited);
              nProvince+=1;
          }
      }  
      return nProvince;
    }
};