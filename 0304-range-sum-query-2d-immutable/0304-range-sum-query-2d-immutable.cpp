class NumMatrix {
public:
    vector<vector<int>> prefixSum;
    NumMatrix(vector<vector<int>>& matrix) {
        int r = matrix.size();
        int c = matrix[0].size();
        prefixSum.resize(r);
        
        for(int i=0;i<r;i++) prefixSum[i].resize(c);
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                prefixSum[i][j] = matrix[i][j];
            }
        }
        for(int i=0;i<r;i++)  {
            for(int j=0;j<c;j++) {
                prefixSum[i][j]+=(j-1>=0)?prefixSum[i][j-1]:0;
            }
        }
         for(int i=0;i<c;i++)  {
            for(int j=0;j<r;j++) {
                prefixSum[j][i]+=(j-1>=0)?prefixSum[j-1][i]:0;
            }
        }
    }
    
  int sumRegion(int row1, int col1, int row2, int col2) {
    int total = prefixSum[row2][col2];
    if (col1 > 0) total -= prefixSum[row2][col1 - 1];
    if (row1 > 0) total -= prefixSum[row1 - 1][col2];
    if (row1 > 0 && col1 > 0) total += prefixSum[row1 - 1][col1 - 1];
    return total;
}
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */