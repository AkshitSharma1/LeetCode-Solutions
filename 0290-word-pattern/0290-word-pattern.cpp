class Solution {
public:
    bool wordPattern(string patterns, string s) {
        vector<string> words;
        string token;
        stringstream ss(s);
        while (getline(ss,token,' ')) {
            words.push_back(token);
        }
        if (words.size()!=patterns.size()) return false;
        unordered_map<char,string> charMap;
        unordered_map<string,char> strMap;
        for(int i=0;i<words.size();i++) {
            if(strMap.find(words[i])==strMap.end() && charMap.find(patterns[i])==charMap.end()) {
                strMap[words[i]]=patterns[i];
                charMap[patterns[i]]=words[i];

            } else if(strMap.find(words[i])!=strMap.end()) {
                if (strMap[words[i]]!=patterns[i]) return false;
            } else if(charMap.find(patterns[i])!=charMap.end() ) {
                if  (charMap[patterns[i]]!=words[i]) return false;
            }
        }
    return true;
    }
};