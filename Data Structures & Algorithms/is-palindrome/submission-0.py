class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower()
        i, j = 0, len(clean)-1
        print(clean)
        while i <= j:
            if clean[i] != clean[j]:
                return False
            i+=1
            j-=1
        return True