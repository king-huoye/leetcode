class Solution:
    def pathEncryption(self, path: str) -> str:
        while '.' in path:
            path=path.replace('.',' ')
        return path
