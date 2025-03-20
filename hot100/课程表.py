class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)#存储链接表
        indegree=[0]*numCourses #记录每个课程的入度
        for dest,src in prerequisites:
            graph[src].append(dest)#src-->dest
            indegree[dest]+=1#
        queue=deque([i for i in range(numCourses) if indegree[i]==0])#入度为0的加入队列
        complete_course=0
        while queue:
            course=queue.popleft()
            complete_course+=1
            for neighbor in graph[course]:#遍历当前课程的邻接节点
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return complete_course==numCourses
