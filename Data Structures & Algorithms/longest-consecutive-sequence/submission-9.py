class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) > 0:
            if len(nums_set) > 1:
                max_streak = 0
                for num in nums_set:
                    current_num = num
                    current_streak = 1
                    if num - 1 not in nums_set:
                        while current_num + 1 in nums_set:
                            current_num += 1  
                            current_streak += 1
                        max_streak = max(max_streak, current_streak)
                return max_streak
            return 1
        return 0