'''Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        sub_s = []
        end = 0
        start = 0
        length = len(s)
        while end < length:
            if s[end] not in sub_s:
                sub_s.append(s[end])
                end += 1
            else:
                sub_s.remove(s[end])
                start += 1
        return end-start

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("bbbbbaccc"))