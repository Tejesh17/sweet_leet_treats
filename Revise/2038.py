class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a = count_b = 0
        for i in range(1, len(colors)-1):
            if(colors[i-1] == colors[i]==colors[i+1]):
                if(colors[i]) == "A":
                    count_a +=1
                else:
                    count_b +=1
        return count_a>count_b