class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        string = list(str(n))  # 将字符串转换为列表
        flag = len(string)
        
        # 从后向前遍历
        for i in range(len(string) - 1, 0, -1):
            if string[i - 1] > string[i]:  # 如果前面的数字大于后面的数字
                string[i - 1] = str(int(string[i - 1]) - 1)  # 前面的数字减1
                flag = i
        
        # 将从标记位置到末尾的数字改为 '9'
        for i in range(flag, len(string)):
            string[i] = '9'
        
        return int(''.join(string))
