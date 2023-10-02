class Solution:
    def reverseWords(self, s: str) -> str:
        spl = s.split(" ")
        for i in range(len(spl)):
            spl[i] = spl[i][::-1]
        return " ".join(spl)