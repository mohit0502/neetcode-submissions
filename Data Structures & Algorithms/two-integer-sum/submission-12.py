class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = sorted(nums)
        l1 = list()
        for i in range(len(nums1)):
            new_target = target-nums1[i]
            index1 = nums.index(nums1[i])
            nums2 = nums1[:i]+nums1[i+1:]
            if new_target in nums2:
                nums3 = nums[:index1]+nums[index1+1:]
                index2_temp = nums3.index(new_target)
                if index2_temp >= index1:
                    target_index = index2_temp + 1
                else:
                    target_index = index2_temp
                l1.append(index1)
                l1.append(target_index)
                return sorted(l1)
            else:
                continue