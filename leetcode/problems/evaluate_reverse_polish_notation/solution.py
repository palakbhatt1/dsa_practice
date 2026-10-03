class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []

        for i in tokens:
            if i not in "+*/-":
                stack.append(int(i))

            else:
                right = stack.pop()
                left = stack.pop()

                if i == "+":
                    j = left + right
                elif i == "-":
                    j = left - right
                elif i == "/":
                    j = int(left / right)
                elif i == "*":
                    j = left * right

                stack.append(j)

        return stack[-1]



