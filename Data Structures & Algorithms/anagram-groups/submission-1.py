class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            key = "".join(sorted(i))
            seen.setdefault(key, []).append(i)
        return list(seen.values())