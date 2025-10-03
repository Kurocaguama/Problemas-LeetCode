class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest_substr = s[0]
        max_len = len(longest_substr)
        for i in range(1, len(s)):
            if s[i] in longest_substr:
                if len(longest_substr) > max_len:
                    max_len = len(longest_substr)
                # Índice de la repetición previa 
                aux = longest_substr.index(s[i])
                longest_substr += s[i]
                longest_substr = longest_substr[aux+1:]
            else:
                longest_substr += s[i]
                if len(longest_substr) > max_len:
                    max_len = len(longest_substr)
        return max_len