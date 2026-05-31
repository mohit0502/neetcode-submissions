class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == '' or s == None:
            return False
        else:
            l1 = list(s)
            l1.sort()
            s1 = "".join(l1)
            l2 = list(t)
            l2.sort()
            t1 = "".join(l2)
            if l1 == l2:
                return True
            else:
                return False