class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int r_ptr = 0;
        int m_ptr = 0;
        sort(ransomNote.begin(),ransomNote.end()); // O(NlogN)
        sort(magazine.begin(),magazine.end()); // O(MlogM)
        while (r_ptr < ransomNote.size() && m_ptr < magazine.size()) { //O(N+M)
            if (ransomNote[r_ptr] == magazine[m_ptr]) {
                m_ptr++;
                r_ptr++;
            }
            else {
                m_ptr++;
            }
        }

        return r_ptr == ransomNote.size();
    }
};
