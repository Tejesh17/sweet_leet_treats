class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        res = []
        j=0
        for i in range(1,n+1):
            if(stack == target):
                return res
            if not stack:
                stack.append(i)
                res.append("Push")
                continue
            while(stack and (stack[-1]!= target[j])):
                stack.pop()
                res.append("Pop")
            stack.append(i)
            res.append("Push")
            if(stack[-1] == target[j+1]):
                j+=1
        return res