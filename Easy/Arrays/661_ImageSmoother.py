class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        rows, cols = len(img), len(img[0])

        for i in range(rows):
            for j in range(cols):
                s = 0
                c = 0
                for I in range(i-1, i+2):
                    for J in range(j-1, j+2):
                        if(I>=0 and I<rows and J>=0 and J<cols):
                            s+=img[I][J]
                            c+=1

                res[i][j] = s//c
        return res