class Solution {
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        vector<int> ans(k,0);
        unordered_map<int,unordered_set<int>> mp;
        for(auto &i: logs){
            mp[i[0]].insert(i[1]);
        }
        unordered_map<int,int> m;
        for(auto &i: mp){
            m[i.second.size()]++;
        }
        for(auto &i: m){
            
            if(i.first<=k)
            ans[i.first-1] = i.second;;
        }
        return ans;
    }
};
