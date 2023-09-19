class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        res = []
        pre.append(nums[0])
        for i in range(1, len(nums)):
            s = nums[i] * pre[-1]
            pre.append(s) 
        post.insert(0, nums[-1])
        for i in range (len(nums)-2, -1, -1):
            s = nums[i] * post[0]
            post.insert(0, s)
        res.append(post[1])
        for i in range(1, len(nums)-1):
            res.append(pre[i-1]* post[i+1])
        res.append(pre[-2])
        return res