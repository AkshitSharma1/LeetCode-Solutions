class Solution {
public:
    bool judgeSquareSum(int c) {
        long long  size=ceil(sqrt(c))+1;
        vector<long long > precomputePower(size,0);
        for(long long  i=0;i<size;i++) {
            precomputePower[i]=i*i;
        }
        long long  l =0;
        long long  r = size-1;
        long long sum=0;
        while(l<=r) {
            sum = precomputePower[l]+precomputePower[r];
            if (sum==c) return true;
            if(sum<c) {
                l+=1;
            } else {
                r-=1;
            }
        }
        return false;
    }
};