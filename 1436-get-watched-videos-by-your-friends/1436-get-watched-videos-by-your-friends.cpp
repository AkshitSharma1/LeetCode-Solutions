class Solution {
public:
    static bool comparator(pair<string,int>& a,pair<string,int>& b) {
        if( a.second==b.second) {
            return a.first<=b.first;
        }
        return a.second<=b.second;
    }
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideos, vector<vector<int>>& friends, int id, int level) {
        int n = friends.size();
        unordered_map<int,int> visited;
        queue<pair<int,int>> q;
    
        q.push({id,0});
        vector<int> levelKFriends;
        visited[id]=1;
        while(!q.empty()) {
            int personId = q.front().first;
            int personLevel = q.front().second;
            q.pop();
            for(auto person:friends[personId]) {
                if(visited.find(person)==visited.end()) {
                    if(personLevel+1==level) {
                        levelKFriends.push_back(person);
                        visited[person]=1;
                    } else {
                        q.push({person,personLevel+1});
                        visited[person]=1;
                    }
                }
            }
        }

        unordered_map<string,int> freq;
        for(auto person:levelKFriends) {
            for(auto watchedVideo:watchedVideos[person]) {
                freq[watchedVideo]++; 
       }
        }
        vector<pair<string,int>> watchedVideoVector;
        for(auto video:freq) {
            watchedVideoVector.push_back({video.first,video.second});
        }
        sort(watchedVideoVector.begin(),watchedVideoVector.end(),comparator);
        vector<string> ans;
        for(auto watchedVideo:watchedVideoVector) ans.push_back(watchedVideo.first);
        return ans;
    }
};