class Solution {
public:
    int balancedStringSplit(string s) {
        int ans = 0;
        int c = 0;
        for(int i = 0; i<s.size();i++){
            if(s[i] == 'L'){
                c++;
            }
            if(s[i] == 'R'){
                c--;
            }
            if(c == 0){
                ans++;
            }
        }
        return ans;
    }
};