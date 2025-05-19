class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations:
            return []
        graph=defaultdict(dict)
        for (a,b),val in zip(equations,values):
            graph[a][b]=val #构建从a到b的带权有向边
            graph[b][a]=1/val
        #构建双向图
        def dfs(start,end,visited,acc):#acc表示累积值
            if start not in graph or end not in graph:
                return -1.0
            if start==end:
                return acc 
            visited.add(start) #避免走回头路
            for neighbor,val in graph[start].items():#寻找是否存在一条路径从start到end
                if neighbor not in visited:
                    res=dfs(neighbor,end,visited,acc*val)
                    if res!=-1.0:
                        return res
            return -1.0
        results=[]
        for x,y in queries:
            results.append(dfs(x,y,set(),1.0))
        return results
        
