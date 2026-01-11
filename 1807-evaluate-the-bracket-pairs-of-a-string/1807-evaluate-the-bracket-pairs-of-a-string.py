class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        answer = []
        temp = []
        key_value_dict = {key:value for key,value in knowledge}
        curr_string = ""
        opening_bracket_found = False
        for char in s:
            if char=="(":
                opening_bracket_found = True
                    
            elif char==")":
                opening_bracket_found = False
                curr_string = "".join(temp)
                if curr_string in key_value_dict:
                    answer.append(key_value_dict[curr_string])
                else:
                    answer.append("?")
                temp.clear()
            else:
                if opening_bracket_found:
                    temp.append(char)
                else:
                    answer.append(char)
        return "".join(answer)





        