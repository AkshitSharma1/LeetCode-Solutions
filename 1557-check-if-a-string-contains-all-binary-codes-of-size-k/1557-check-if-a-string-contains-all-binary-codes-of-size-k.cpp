class Solution {
public:
    bool hasAllCodes(string s, int k) {
    int need = 1 << k;
    unordered_set<string> got;

    for (int i = k; i <= s.size(); i++) {
        got.insert(s.substr(i - k, k));
        if (got.size() == need) {
            return true;
        }
    }

    return false;
    }
};