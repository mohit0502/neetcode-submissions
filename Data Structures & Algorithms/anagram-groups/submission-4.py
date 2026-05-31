class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            # Use sorted word as the key
            key = ''.join(sorted(word))
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]
        
        # Collect all groups from the dictionary
        return list(anagram_map.values())