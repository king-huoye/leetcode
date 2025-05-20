class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        genes=['A','C','G','T']
        bank_set=set(bank)
        que=deque([(startGene,0)])#创建一个元组
        visited=set()
        while que:
            gene,step=que.popleft()
            if gene==endGene:
                return step #找到了
            for i in range(len(gene)):
                for ch in genes:
                    if ch==gene[i]:
                        continue
                    mutated=gene[:i]+ch+gene[i+1:] #字符串拼接
                    if mutated in bank_set and mutated not in visited:
                        visited.add(mutated)
                        que.append((mutated,step+1))
        return -1
