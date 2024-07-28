class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int p1=0;
        int p2=1;
        
       
        int n = nums.size();
        int notEqualVal=0;
        for(auto num:nums) {
            if(num!=val) notEqualVal+=1;
        }
        if(n==0) return 0;
        if(n==1) {
            if(nums[0]==val) return 0;
            return 1;
        }
        while(p1<n) {
            cout<<"num is "<<endl;
            for(auto num:nums) cout<<num<<" ";
            cout<<endl;
            p2=p1+1;
            if(nums[p1]!=val) {
                p1+=1;
                p2+=1;
                continue;
            } else if(nums[p1]==val) {
                cout<<p1<<" p1 with nums[p1]: "<<nums[p1]<<" is equal to val"<<endl;
                //Ascend second pointer till we do not have val
                while(p2<n&&nums[p2]==val) {p2+=1;}
                if(p2==n) { 
                    return notEqualVal;
                    }
                while(p1<n&& p2<n&&nums[p1]==val && nums[p2]!=val) {
                    cout<<"swap p1 :"<<p1<<" and p2: "<<p2 <<endl;
                    swap(nums[p1],nums[p2]);
                    p1+=1;
                    p2+=1;
                }
            }

        }
        return notEqualVal;
    }
};