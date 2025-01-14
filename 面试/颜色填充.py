class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        
        origin = image[sr][sc]
        
        # 如果起始像素已经是目标颜色，直接返回图像
        if origin == newColor:
            return image
        
        def dfs(r, c):
            # 越界检查
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return 
            # 如果当前像素的颜色不是原始颜色，或者已经改变颜色，直接返回
            if image[r][c] != origin:
                return 
            
            # 改变当前像素的颜色
            image[r][c] = newColor
            
            # 递归四个方向
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # 从起始位置开始递归
        dfs(sr, sc)
        
        return image
