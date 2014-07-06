class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        a1 = 0
        for x in tokens:
            if(x == '+'):
                a1 = stack.pop()
                a2 = stack.pop()
                a1 = a1 + a2
            elif(x == "-"):
                a1 = stack.pop()
                a2 = stack.pop()
                a1 = a2 - a1
            elif(x == '*'):
                a1 = stack.pop()
                a2 = stack.pop()
                a1 = a1 * a2
            elif(x == '/'):
                a1 = stack.pop()
                a2 = stack.pop()
                a1 = int(float(a2)/a1)
            else:
                a1 = int(x)
            stack.append(a1)
        return int(stack.pop())

s = Solution()
l = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(l)
