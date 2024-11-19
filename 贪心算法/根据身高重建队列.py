class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        result=[]
        for p in people:
            result.insert(p[1],p)#指定索引插入位置,在位置p[1]插入元素P
        return result
