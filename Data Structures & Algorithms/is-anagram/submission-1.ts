class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const characterCounts = new Map<string, number>()
        for (const char of s) {
            if (characterCounts.has(char)) characterCounts.set(char, characterCounts.get(char) + 1)
            else characterCounts.set(char, 1)
        }
        const characterCount = new Map<string, number>()
        for (const char of t) {
            if (characterCount.has(char)) characterCount.set(char, characterCount.get(char) + 1)
            else characterCount.set(char, 1)
        }
        if (characterCount.size !== characterCounts.size) return false
        let equivelent = true
        for (const char of characterCount.keys()) {
            equivelent = characterCount.get(char) === characterCounts.get(char)
            if (!equivelent) return false
        }
        return true
    }
}
