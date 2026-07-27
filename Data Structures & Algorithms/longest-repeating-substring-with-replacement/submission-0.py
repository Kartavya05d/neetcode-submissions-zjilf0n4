class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, l = 0, 0
        count = [0]*26

        for r in range(len(s)):
            count[ord(s[r])-ord('A')] += 1 #update frequency [add new character]
            #We will consider to replace the chars in minority.
            while (r-l+1) - max(count) > k: # current window lenght - number of majority elements.
                #shorten the window : current window is ineligible.
                count[ord(s[l])-ord('A')] -= 1
                l+=1
            longest = max(longest, r-l+1)
        return longest
