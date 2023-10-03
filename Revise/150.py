class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack.append(float(tokens[0]))
        ops={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for i in range(1,len(tokens)):
            if(tokens[i] in ops):
                op2 = stack.pop()
                op1 = stack.pop()
                res = int(ops[tokens[i]](op1, op2))
                stack.append(res)
            else: 
                stack.append(float(tokens[i]))
        return int(stack[0])                        