class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr)/4
        h = {}
        for i in arr:
            h[i] = h.get(i,0)+1
            if(h[i] > threshold):
                return i