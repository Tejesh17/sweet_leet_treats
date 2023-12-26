class Solution:
    def minOperations(self, s: str) -> int:
        count_odd = count_even = 0
        for i, v in enumerate(s):
            if(i%2 ==0):
                if(v == "0"):
                    count_even+=1
                else:
                    count_odd+=1
            else:
                if(v == "1"):
                    count_even+=1
                else:
                    count_odd +=1
        return min(count_even, count_odd)