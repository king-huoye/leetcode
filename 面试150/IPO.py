import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        num_projects = len(profits)
        project_list = []
        
        # 将每个项目的资本需求和对应利润配对
        for i in range(num_projects):
            project_list.append([capital[i], profits[i]])
        
        # 按所需资本升序排序
        project_list.sort()
        
        max_profit_heap = []  # 最大堆，用于存储可选项目的利润（取负值实现最大堆）
        project_index = 0
        available_capital = w
        
        for _ in range(k):
            # 将当前资本可承受的项目加入最大堆
            while project_index < num_projects and project_list[project_index][0] <= available_capital:
                heapq.heappush(max_profit_heap, -project_list[project_index][1])
                project_index += 1
            
            if not max_profit_heap:
                break  # 没有可选项目，退出循环
            
            # 选择利润最高的项目
            max_profit = -heapq.heappop(max_profit_heap)
            available_capital += max_profit
        
        return available_capital
