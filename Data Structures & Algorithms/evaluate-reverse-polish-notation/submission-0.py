import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])
        stack = []
        operations = ["+", "-", "*", "/"]
        for i in tokens:
            if i in operations:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if i == "+":
                    stack.append(n1 + n2)
                    continue
                elif i == "-":
                    stack.append(n1 - n2)
                    continue
                elif i == "*":
                    stack.append(n1 * n2)
                    continue
                else:
                    n = n1 / n2
                    if n < 0:
                        stack.append(math.ceil(n))
                    else:
                        stack.append(math.floor(n))
                    continue
            stack.append(i)
        return(stack[-1])