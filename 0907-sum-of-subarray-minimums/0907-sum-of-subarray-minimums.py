class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        NSR = [n]*n
        NSL = [-1]*n
        NSR_stack = []
        NSL_stack = []
        #first do nsr-> start right to left and we keep a monotonic increasing stack
        for r in range(n-1,-1,-1):
            while NSR_stack and arr[NSR_stack[-1]]>=arr[r]:
                NSR_stack.pop()
            
            if NSR_stack:
                NSR[r] = NSR_stack[-1]
            
            NSR_stack.append(r)

        #now we do nsl-> start from left to right, keep monotonic increasing stack
        for r in range(0,n,1):
            while NSL_stack and arr[NSL_stack[-1]]>arr[r]:
                NSL_stack.pop()
            
            if NSL_stack:
                NSL[r] = NSL_stack[-1]
            
            NSL_stack.append(r)
        
        ans = 0
        mod = 10**9+7
        for r in range(0,n,1):
            ans += (r-NSL[r])*(NSR[r]-r)*arr[r]
            ans%=mod
        return ans


