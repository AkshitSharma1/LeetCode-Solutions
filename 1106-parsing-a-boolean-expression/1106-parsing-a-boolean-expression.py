class Solution:
    def evaluate_exp(self,operand,expression):
        if operand=='&':
            for c in expression:
                if c=='f': return "f"
            return "t"
        elif operand=='!':
            if expression[0]=='f': return "t"
            return "f"
        elif operand=='|':
            for c in expression:
                if c=='t': return "t"
            return "f"
        return "f"

    def parseBoolExpr(self, expression: str) -> bool:
        operation_stack = []
        evaluation_stack = []
        for ch in expression:
            if ch in ('!','&','|'):
                    operation_stack.append(ch)
            elif ch==')':
                curr_string_stack = []
                while evaluation_stack[-1]!="(":
                    curr_string_stack.append(evaluation_stack.pop())
                evaluation_stack.pop()
                evaluation_stack.append(self.evaluate_exp(operation_stack.pop(),"".join(curr_string_stack)))
            else:
                evaluation_stack.append(ch)
        return False if evaluation_stack[0]=="f" else True
		

      

