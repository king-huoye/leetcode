class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 用于存储当前窗口中的字符
        left = 0          # 滑动窗口的左边界
        ans = 0           # 记录最长无重复字符子串的长度

        for right in range(len(s)):
            while s[right] in char_set:  # 如果当前字符已存在，移动左边界
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])  # 将当前字符加入集合
            ans = max(ans, right - left + 1)  # 更新最大长度

        return ans
