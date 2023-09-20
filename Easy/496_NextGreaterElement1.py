class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            ind = nums2.index(nums1[i])
            j = ind+1
            k = -1
            for j in range(ind+1, len(nums2)):
                if(nums2[j]> nums1[i]  ):
                    k = j
                    break
            if (k == -1):
                res.append(-1)
            else:
                res.append(nums2[k])
        return res