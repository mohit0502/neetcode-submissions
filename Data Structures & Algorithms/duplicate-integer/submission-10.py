class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            for i in range(len(nums)):
                k=False
                temp = nums[:i]+nums[i+1:]
                if nums[i] in temp:
                    k=True
                    break
            return k
        else:
            return False