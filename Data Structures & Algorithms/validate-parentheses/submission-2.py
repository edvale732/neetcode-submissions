class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, char in enumerate(s):
            if stack != []:
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        print(stack)
        if stack == []:
            return True
        
        return False

    