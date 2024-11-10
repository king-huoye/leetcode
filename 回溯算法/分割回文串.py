class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.path=[]
        self.result=[]
        def backtracking(Str, startIndex):
            # 如果当前分割的最后一个部分是回文，则将当前分割加入结果
            if startIndex == len(Str):
                self.result.append(self.path[:])  # 深拷贝当前路径
                return #收集结果
            
            for i in range(startIndex, len(Str)):
                # 取子串并检查是否是回文
                substring = Str[startIndex:i+1]
                if substring == substring[::-1]:  # 如果是回文
                    self.path.append(substring)  # 将回文子串加入当前路径
                    backtracking(Str, i + 1)     # 递归到下一个位置
                    self.path.pop()              # 回溯，移除最后一个子串

        backtracking(s, 0)
        return self.result
        
