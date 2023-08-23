class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        words= {}
        words['b']=0;
        words['a']=0
        words['l']=0
        words['o']=0
        words['n'] = 0
        for i in text:
            if(i in'balon'):
                words[i] = 1+ words[i]
        if((words['b']>0 and  words['a'] >0 and  math.floor(words['l']/2) >0 and  math.floor(words['o']/2) >0 and  words['n']>0)):
            words['l'] =math.floor(words['l']/2)
            words['o'] =math.floor(words['o']/2)
            return (words[str(min(words, key=words.get))])
        return 0