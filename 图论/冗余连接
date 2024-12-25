class Union:
    def __init__(self, n):
        self.father = list(range(n + 1))
    
    def find(self, u):
        if self.father[u] == u:
            return u 
        else:
            return self.find(self.father[u])
    
    def un(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.father[root_u] = root_v
    
    def isSame(self, u, v):
        return self.find(u) == self.find(v)

if __name__ == '__main__':
    n = int(input())  # 读取一个整数，表示节点的数量
    Ma = Union(n)
    
    result = []  # 用来保存结果的列表
    for i in range(n):
        s, t = map(int, input().split())  # 输入两个整数
        if Ma.isSame(s, t):
            result.append(f"{s} {t}")  # 如果是同一个集合，保存结果
        else:
            Ma.un(s, t)  # 否则合并两个集合
    
    # 打印所有结果
    if result:
        print("\n".join(result))
