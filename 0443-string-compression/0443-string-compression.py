class Solution:
    def compress(self, chars: List[str]) -> int:
        insertionIndex = 0
        currentChar = -1
        currentCharLength = 0
        for r,char in enumerate(chars):
            if char==currentChar:
                currentCharLength+=1
            else:
                #Add this to the array
                if currentChar!=-1:
                    chars[insertionIndex] = currentChar
                    insertionIndex+=1
                    if currentCharLength>1:
                        splittedCharLength = list(str(currentCharLength))
                        for charLength in splittedCharLength:
                            chars[insertionIndex] = str(charLength)
                            insertionIndex+=1
                currentChar = char
                currentCharLength = 1
        if currentChar!=-1:
                chars[insertionIndex] = currentChar
                insertionIndex+=1
                if currentCharLength>1:
                    splittedCharLength = list(str(currentCharLength))
                    for charLength in splittedCharLength:
                        chars[insertionIndex] = str(charLength)
                        insertionIndex+=1

                currentChar = char
                currentCharLength = 1
        
        return insertionIndex

        