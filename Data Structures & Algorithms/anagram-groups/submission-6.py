class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            if (tuple(count) not in map):
                map[tuple(count)] = []
            map[tuple(count)].append(str)
        for value in map.values():
            res.append(value)
        return res
