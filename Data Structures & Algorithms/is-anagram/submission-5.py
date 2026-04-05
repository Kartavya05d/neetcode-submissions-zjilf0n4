class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_1 = {}
        hashmap_2 = {}
        for i in range(len(s)):
            hashmap_1[s[i]] = hashmap_1.get(s[i], 0) + 1
            hashmap_2[t[i]] = hashmap_2.get(t[i], 0) + 1
        return hashmap_1 == hashmap_2
