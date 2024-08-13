class Solution {
public:


    bool wordsDifferByOneLetter(string& s1,string &s2) {
        int count=0;
        if(s1.length()!=s2.length()) return false;
        for(int i=0;i<s1.length();i++) {
            if(s1[i]!=s2[i]) count++;
            if (count>1) return 0;
        }
        return true;
    }


    bool dfs(int targetInd,int currentInd,vector<int>& visited,vector<vector<int>>& adjList,vector<string>& wordList,vector<vector<string>> &ans,vector<string>& temp,int dist,vector<vector<int>>& dp) {

        if(dist<0) {
            return false;
        }

        if(dp[currentInd][dist]==0) return false;
        
        visited[currentInd]=1;
        temp.push_back(wordList[currentInd]);
        if(currentInd==targetInd && dist==0) {
            ans.push_back(temp);
            temp.pop_back();
            visited[currentInd]=0;
            return true;
        }
        bool output=false;
        for(int neighbour:adjList[currentInd]) {
            if(visited[neighbour]==0) {
                    if(dfs(targetInd,neighbour,visited,adjList,wordList,ans,temp,dist-1,dp)) {
                        output=true;
                    }
                }
            }
            dp[currentInd][dist]=output;
        
        visited[currentInd]=0;
        temp.pop_back();
        return output;
    }
    

    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
                vector<vector<string>> ans;

        if (find(wordList.begin(),wordList.end(),beginWord)==wordList.end()) wordList.insert(wordList.begin(),beginWord);
        if (find(wordList.begin(),wordList.end(),endWord)==wordList.end()) return ans ; //doesnt exist
        int startInd =  find(wordList.begin(),wordList.end(),beginWord)-wordList.begin();
        int targetInd = find(wordList.begin(),wordList.end(),endWord)-wordList.begin();
        int n = wordList.size();
        //We will form a graph using adjacency list and apply bfs on it
        vector<vector<int>> adjList(n);
        for(int i=0;i<n;i++) {
            for(int j=i+1;j<n;j++) {
                if(wordsDifferByOneLetter(wordList[i],wordList[j])) {
                    adjList[i].push_back(j);
                    adjList[j].push_back(i);
                }
            }
        }

        //Time complexity of above is O(n^2k), k is max length of string
        //Now bfs
        vector<int> visited(n,0);
        vector<int> dist(n,-1);
        queue<int> q;
        q.push(startInd);
        dist[startInd]=0;

        while(!q.empty()) {
            int node = q.front();
            q.pop();
            for(auto adj:adjList[node]) {
                if(dist[adj]==-1) {
                    q.push(adj);
                    dist[adj]=dist[node]+1;
                }
            }

        }
        if(dist[targetInd]==0) return ans;
        vector<string> temp;
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        dfs(targetInd,startInd,visited,adjList,wordList,ans,temp ,dist[targetInd],dp);
        return ans;
    }
};