class Solution(object):
    def truncateSentence(self, s, k):
        helll = s.split(' ')
        x= slice(k)
        
        word = ' '.join(helll[x])
        return word