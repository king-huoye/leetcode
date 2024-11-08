class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path=[]
        self.result=[]
        def fun(n,k,index):
            if len(self.path)==k:
                self.result.append(self.path[:])
                return 
            for i in range(index,n+1):
                self.path.append(i)
                fun(n,k,i+1)
                self.path.pop()
        fun(n,k,1)
        return self.result
        
