class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        visited=[False]*n
        table=defaultdict(list)
        for u,v in graph:
            table[u].append(v)#建立邻接表
        def dfs(node):
            if node==target:
                return True #访问到
            visited[node]=True
            for neighbor in table[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start)
