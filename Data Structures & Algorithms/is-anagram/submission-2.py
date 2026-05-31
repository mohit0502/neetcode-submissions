class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        l1 = [i for i in s]
        l1.sort()
        l2 = [i for i in t]
        l2.sort()
        if len(l1)==len(l2):
            if l1==l2:
                return True
            else:
                return False
        else:
            return False
        