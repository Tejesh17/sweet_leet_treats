class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li, hi = 0, len(matrix)-1
        while (li<= hi):
            mid = (li+hi)//2
            if(target< matrix[mid][0]):
                hi = mid -1
            elif(target > matrix[mid][-1]):
                li = mid +1
            else:
                lo, ho = 0, len(matrix[mid])-1
                while(lo<=ho):
                    mo = (lo+ho)//2
                    if (matrix[mid][mo] == target):
                        return True
                    elif(target > matrix[mid][mo]):
                        lo = mo +1
                    else:
                        ho = mo -1
                return False
        return False 