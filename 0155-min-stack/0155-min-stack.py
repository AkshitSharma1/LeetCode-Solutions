class MinStack:

    def __init__(self):
        self.min_stack = []
        self.normal_stack = []
        

    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1],val))
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        self.min_stack.pop()
        return self.normal_stack.pop()    

    def top(self) -> int:
        return self.normal_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()