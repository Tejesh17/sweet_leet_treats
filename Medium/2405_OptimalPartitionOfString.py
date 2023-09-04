class Solution:
    def partitionString(self, s: str) -> int:
        sol = []
        word=""
        for i in s:
            if(i not in word):
                word+=i
            else:
                sol.append(word)
                word = i
        if word != "":
            sol.append(word)
        return len(sol)