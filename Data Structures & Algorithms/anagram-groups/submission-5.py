class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for str in strs:
            count = [0] * 26

            for s in str:
                count[ord(s) - ord('a')] += 1

            key = tuple(count)

            if (key not in map):
                map[key] = []

            map[key].append(str)

        return list(map.values())

