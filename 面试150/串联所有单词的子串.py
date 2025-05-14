class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []

        for i in range(word_len):  # 处理不同的起点情况
            left = i
            right = i
            curr_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr_count[word] += 1

                    # 超过预期次数，需要左边收缩窗口
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                    
                    if right - left == total_len:
                        res.append(left)
                else:
                    # 不在目标单词中，清空窗口
                    curr_count.clear()
                    left = right
        return res
