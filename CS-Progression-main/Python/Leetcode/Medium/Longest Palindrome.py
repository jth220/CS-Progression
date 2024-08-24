class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        res = ""

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    res = s[l:r+1]
                    maxLength = r - l + 1
                l -= 1
                r += 1
           
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    res = s[l:r+1]
                    maxLength = r - l + 1
                l -= 1
                r += 1
        return res
        
        #For everytime it traverses through the string, left and right pointer
        #is constantly checking if they match, and they expand if they do
        