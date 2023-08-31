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
        highest = arr[-1];
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1 ):
            if arr[i]> highest:
                arr[i], highest = highest, arr[i]
            else:
                arr[i] = highest
        return arr