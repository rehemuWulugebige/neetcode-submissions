class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) return false

        let countS = {}
        let countT = {}

        for (let i = 0; i < s.length; i++) {
            countS[s[i]] = (countS[s[i]] || 0) + 1
            countT[t[i]] = (countT[t[i]] || 0) + 1
        }

        for (let str in countS) {
            if (countS[str] != countT[str]) {
                return false
            }
        }

        return true
    }
}
