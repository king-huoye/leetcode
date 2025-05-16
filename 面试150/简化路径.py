class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for part in path.split('/'):
            if part=='' or part=='.':
                continue
            elif part=='..':不会让路径返回根目录之上
                if stack:
                    stack.pop()
            else:
                stack.append(part) #合法路径才加入
        return '/'+'/'.join(stack)
