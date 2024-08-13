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
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
         if (find(wordList.begin(),wordList.end(),beginWord)==wordList.end()) wordList.insert(wordList.begin(),beginWord);
        if (find(wordList.begin(),wordList.end(),endWord)==wordList.end()) return 0; //doesnt exist
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
                    cout<<"dist is node: "<<dist[node]<<" while adj: "<<dist[adj]<<endl;
                }
            }

        }
        return (dist[targetInd]==0)?0:dist[targetInd]+1;
    }
};