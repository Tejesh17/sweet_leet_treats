class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # p = len(arr)
        # for i in range(p-1):
        #     greatest = arr[i+1]
        #     for x in range(i+1, p):
        #         if arr[x] > greatest:
        #             greatest = arr[x]
        #     arr[i] = greatest
        # arr[p-1] = -1
        # return arr
        largest = arr[len(arr)-1]
        arr[len(arr)-1] = -1 
        for i in range(len(arr)-2, -1, -1):
            temp = 0
            if(arr[i])> largest:
                temp = arr[i]
            arr[i] = largest 
            if(temp>0):
                largest = temp
        return arr