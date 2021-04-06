class Solution(object):
    def totalMoney(self, n):
        weeks = n/7
        leftover = n%7
        sum= 0 
        x = range(4,weeks+4)
        for i in x:
            sum += 7*i
        x= range(weeks+1, weeks+leftover+1)
        for i in x:
            sum +=i
        return sum
