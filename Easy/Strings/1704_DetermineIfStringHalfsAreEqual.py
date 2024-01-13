class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first, last = 0,0
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        for i,l in enumerate(s):
            if l in vowels:
                if i <len(s)//2:
                    first +=1
                else:
                    last +=1
        return first == last