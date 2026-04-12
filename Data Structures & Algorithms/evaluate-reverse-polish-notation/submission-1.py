from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in '+-*/':
                b, a = stack.pop(), stack.pop()
                if x == '+':
                    stack.append(a+b)
                elif x == '-':
                    stack.append(a-b)
                elif x == '*':
                    stack.append(a*b)
                else:
                    div = a/b
                    if (div<0):
                        stack.append(ceil(div))
                    else:
                        stack.append(floor(div))
            else:
                stack.append(int(x))
        return stack[0]