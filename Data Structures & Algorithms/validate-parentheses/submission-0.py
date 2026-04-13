class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")" : "(" , "}" : "{" , "]" : "["}
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i in matches:
                if stack and stack[-1] == matches[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False   
        