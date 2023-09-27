class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ha={}
        for i in range(len(nums)):
            if( nums[i] in ha and abs(i- ha[nums[i]])<=k):
                return True
            ha[nums[i]] = i
        return False