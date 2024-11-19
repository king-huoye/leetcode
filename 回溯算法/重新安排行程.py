class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)#空字典,列表的格式
        for F,to in sorted(tickets,reverse=True):
            graph[F].append(to)
        result=[]
        def dfs(airport):
            while graph[airport]:
                next=graph[airport].pop()
                dfs(next)
            result.append(airport)
        dfs('JFK')
        return result[::-1]#后序遍历,栈的形式
