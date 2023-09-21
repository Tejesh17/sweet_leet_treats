class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        i, j = 0, len(people)-1
        while(i<=j):
            if(people[i]+people[j] > limit):
                res+=1
                j-=1
            else:
                res+=1
                j-=1
                i+=1
        return res