class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacement_dict = {key:value for key,value in replacements}
        stack = []
        temp = []
        seen_sign_count = 0
        for char in text:
            if char=='%':
                if seen_sign_count==0:
                    stack.append(char)
                    seen_sign_count+=1
                elif seen_sign_count==1:
                    temp = []
                    seen_sign_count = 0
                    while stack and stack[-1]!='%':
                        temp.append(stack.pop())
                    stack.pop()
                    curr_string = "".join(temp)
                    if curr_string in replacement_dict:
                        stack.append(self.applySubstitutions(replacements,replacement_dict[curr_string]))

            else:
                stack.append(char)
        return "".join(stack)


