class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = {}
        for i, n in enumerate(strs):
            l1 = [n]
            temp = strs[:i]+strs[i+1:]
            for m in temp:
                if "".join(sorted(n)) == "".join(sorted(m)):
                    l1.append(m)

            indices[i] = sorted(l1)

        final_list = list(indices.values())
        unique_data = [list(i) for i in set(tuple(i) for i in final_list)]
        
        return unique_data