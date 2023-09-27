class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        s = 0
        i=0
        for j in range(len(arr)):
            s += arr[j]
            while (j-i >k-1):
                s -= arr[i]
                i+=1
            if(s/k >= threshold and j-i == k-1):
                c+=1
        return c