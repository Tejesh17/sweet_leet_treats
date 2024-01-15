class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count_hash = {}
        players = set()
        res = [[],[]]
        for m in matches:
            players.add(m[0])
            players.add(m[1])
            count_hash[m[1]] = count_hash.get(m[1],0) +1
        players = list(players)
        players.sort()
        for i in players:
            if(i not in count_hash):
                res[0].append(i)
            elif(count_hash[i] ==1):
                res[1].append(i)
        return res