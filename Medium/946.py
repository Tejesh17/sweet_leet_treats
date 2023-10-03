class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        while(i<len(pushed)):
            stack.append(pushed[i])
            if stack!= []:
                while (j< len(popped) and stack!= [] and popped[j] == stack[-1] ):
                    stack.pop()
                    j+=1
            i+=1
        return j == len(popped)