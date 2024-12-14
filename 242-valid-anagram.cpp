class Solution {
public:
    // Time: O(N)
    // Space: O(1)
    bool isAnagram(string s, string t) {
        size_t sc[26] = {0};
        size_t tc[26] = {0};

        for (auto c : s) { sc[tolower(c) - 'a']++; }
        for (auto c : t) { tc[tolower(c) - 'a']++; }

        for (size_t i = 0; i < 26; i++) {
    	    if (sc[i] != tc[i]) {
    	        return false;
	        }
        }

        return true;
    }
};
