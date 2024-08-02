class StockSpanner {
public:
    stack<pair<int,int>> st;
    StockSpanner() {
        
    }
    
    int next(int price) {
        if(st.empty()) {
            st.push({price,1});
            return 1;
        } else{
            //Stack is not empty
            int count=1;
            while(st.empty()==false && st.top().first<=price) {
                count+=st.top().second;
                st.pop();
            }
            st.push({price,count});
            return count;
        }
        return -1;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */