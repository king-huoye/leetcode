class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for dest,src in prerequisites:
            graph[src].append(dest)
            indegree[dest]+=1
        que=deque([i for i in range(numCourses) if indegree[i]==0])
        result=[]
        complete=0
        while que:
            course=que.popleft()
            result.append(course)
            complete+=1
            for neighbor in graph[course]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    que.append(neighbor)
                    
        return result if numCourses==complete else []
