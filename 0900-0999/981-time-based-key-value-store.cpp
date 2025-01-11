class TimeMap {
public:
    TimeMap() {
        
    }
    vector<pair< string, pair<string, int>>> v;
    
    void set(string key, string value, int timestamp) {
        pair<string, int> p = {value, timestamp};
        pair<string, pair<string, int> > p1 = {key, p};
        v.push_back(p1);
   
    }
    
    string get(string key, int timestamp) {
        for(int i=v.size()-1; i>=0; i--) {
            if(v[i].first==key) {
                if(v[i].second.second==timestamp) {
                    return v[i].second.first;
                }
                else if(v[i].second.second<timestamp) {
                    return v[i].second.first;
                }
            }
        }
        return "";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
