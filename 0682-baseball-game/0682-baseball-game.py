class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation=='+':
                n1= stack[-1]
                n2 = stack[-2]
                stack.append(n1+n2)
            elif operation=='D':
                stack.append(stack[-1]*2)
            elif operation=='C': stack.pop()
            else: stack.append(int(operation))
        return sum(stack)