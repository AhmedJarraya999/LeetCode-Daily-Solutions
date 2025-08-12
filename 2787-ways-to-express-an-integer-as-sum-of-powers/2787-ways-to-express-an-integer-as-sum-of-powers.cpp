class Solution {
    #define MOD 1000000007
    vector<int> value;
    int mem[300+2][300+2];

    int binaryExponentiation(int a,int b){
        int res = 1;
        while(b){
            if(b&1)
                res *= a;
            a *= a;
            b /= 2;
        }
        return res;
    }
    int findWays(int pos,int target){
        if(target==0)                           return 1;//Valid combination
        if(pos==value.size() or target<0)       return 0;//Invalid
        if(mem[pos][target]!=-1)                return mem[pos][target];

        int exclude = findWays(pos+1,target);
        int include = findWays(pos+1,target-value[pos]);
        return mem[pos][target] = (exclude + include) % MOD;
    }
public:
    int numberOfWays(int n, int x) {
        for(int i=1;i<=n;++i){
            int power = binaryExponentiation(i,x);
            if(power>n)//Can't include any more powers
                break;
            
            value.push_back(power);
        }
        memset(mem,-1,sizeof(mem));
        return findWays(0,n);
    }
};
