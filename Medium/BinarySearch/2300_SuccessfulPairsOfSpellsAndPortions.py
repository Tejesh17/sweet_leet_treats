class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        for spell in spells:
            l,h= 0, len(potions)-1
            while(l<=h):
                mid = (l+h)//2
                if( spell* potions[mid] >=success):
                    h = mid-1
                else:                    
                    l=mid+1
            res.append(len(potions)- l)
        return res