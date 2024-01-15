class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1= Counter(word1)
        w2 = Counter(word2)
        w1l = list(w1.values())
        w2l = list(w2.values())
        w1l.sort()
        w2l.sort()
        return w1l  == w2l and w1.keys() == w2.keys()