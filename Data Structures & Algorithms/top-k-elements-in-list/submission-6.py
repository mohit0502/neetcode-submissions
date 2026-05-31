class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_elements = {}
        for i in nums:
            count_elements[i] = 1 + count_elements.get(i, 0)
        if k>=len(count_elements):
            return list(count_elements.keys())
        sorted_dict = dict(sorted(count_elements.items(), key=lambda item: item[1]))
        l1 = list(sorted_dict.keys())
        return l1[-k:]