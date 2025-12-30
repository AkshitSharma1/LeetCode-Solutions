class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token=="*":
                n1,n2 = stack.pop(),stack.pop()
                stack.append(n1*n2)
            elif token=='+':
                n1,n2 = stack.pop(),stack.pop()
                stack.append(n1+n2)
            elif token=='-':
                n1,n2 = stack.pop(),stack.pop()
                stack.append(n2-n1)
            elif token=='/':
                n1,n2 = stack.pop(),stack.pop()
                stack.append(int(n2/n1))
            else:
                stack.append(int(token))
        return stack[-1]


        