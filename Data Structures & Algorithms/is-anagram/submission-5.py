class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        mapS, mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1

        for key in mapS:
            if (mapS[key] != mapT.get(key, 0)):
                return False

        return True
