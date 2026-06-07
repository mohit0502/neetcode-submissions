class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        l1 = []
        for i in range(len(nums_sorted)):
            new_target = 0 - nums_sorted[i]
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            left = i+1
            right=len(nums)-1
            while left<right:
                if nums_sorted[left]+nums_sorted[right]>new_target:
                    right-=1
                elif nums_sorted[left]+nums_sorted[right]<new_target:
                    left+=1
                elif nums_sorted[left]+nums_sorted[right]==new_target:
                    l1.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    while left < right and nums_sorted[left] == nums_sorted[left + 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right - 1]:
                        right -= 1
                    left+=1
                    right-=1
        return l1