class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:

        uniques = {}
        
        for c in enumerate(s):
            if c not in uniques:
                uniques[c]




a = "abcabcbb"
b = "bbbbb"
c = "pwwkew"

print(Solution.lengthOfLongestSubstring(a))