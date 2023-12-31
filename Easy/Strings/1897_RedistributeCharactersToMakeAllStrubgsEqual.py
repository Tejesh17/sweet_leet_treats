class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        w_hash= {}
        for i in words:
            for w in i:
                w_hash[w] = w_hash.get(w, 0)+1
        for w in w_hash:
            if w_hash[w]% len(words) != 0:
                return False
        return True 