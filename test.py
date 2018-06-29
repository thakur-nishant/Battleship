class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        location = {}
        max_len = 0
        j = 0

        if len(s) == 1:
            return 1
        for i in range(len(s)):
            if s[i] in location:
                j = max(j, location[s[i]])
            location[s[i]] = i + 1
            max_len = max(max_len, i - j + 1)

        return max_len

s = "abba"
x = Solution().lengthOfLongestSubstring(s)
print(x)
