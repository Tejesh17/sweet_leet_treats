class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                n = stack[-1]
                if (i == ")" and n =="("):
                    stack.pop(-1)
                elif (i == "}" and n =="{"):
                    stack.pop(-1)
                elif (i == "]" and n =="["):
                    stack.pop(-1)
                else:
                    return False
        if(len(stack)== 0 ):
            return True