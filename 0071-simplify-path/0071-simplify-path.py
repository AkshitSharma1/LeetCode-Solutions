class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        for char in path+"/":
            if char!="/":
                curr+=char
            else:
                if curr=="" or curr==".":
                    curr = ""
                    continue
                elif curr=="..":
                    if stack: stack.pop()
                else:
                    stack.append(curr)
                curr = ""
        return "/"+"/".join(stack)
                