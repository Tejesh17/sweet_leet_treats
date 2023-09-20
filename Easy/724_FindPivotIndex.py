class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = []
        post = []
        pre.append(0)
        pre.append(nums[0])
        for i in range(1, len(nums)):
            pre.append(pre[-1]+ nums[i])
        post.append(nums[-1])        
        post.append(0)
        for i in range( len(nums)-2, -1, -1):
            post.insert(0, post[0]+ nums[i])
        for i in range(1,len(pre)):
            if(pre[i-1]==post[i]):
                return i-1
        return -1