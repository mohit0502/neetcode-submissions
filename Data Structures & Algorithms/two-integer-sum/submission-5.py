class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)>2:
            for i in range(len(nums)):
                new_list = nums[:i] + nums[i + 1:]
                for j in range(len(new_list)):
                    if nums[i]+new_list[j] == target:
                        # l = nums.index(new_list[j]) if new_list[j] in nums else None
                        l = [k for k in range(len(nums)) if nums[k] == new_list[j]]
                        if len(l)==2:
                            return [i, l[1]]
                        else:
                            return [i, l[0]]
        else:
            return [0, 1]