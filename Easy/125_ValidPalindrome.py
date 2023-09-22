class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")
        i, j = 0, len(s)-1
        l = [i for i in range(97,123)]
        p=["0","1","2","3","4","5","6","7","8","9"]
        for i in s:
            if((ord(i) not in l) and (i not in p)):
                s= s.replace(str(i), "")
        return s == s[::-1]