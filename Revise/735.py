class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1]>0 and a <0:
                if(stack[-1] > -a):
                    break
                elif(stack[-1] == -a):
                    stack.pop()
                    break
                elif(stack[-1]< -a):
                    stack.pop()
                    continue
            else:
                stack.append(a)
        return stack