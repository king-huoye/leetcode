
def judge(s1,s2):
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1 
    return count==1

if __name__ == '__main__':
    n=int(input())
    beginStr,endStr=map(str,input().split())
    if beginStr==endStr:#一样就不用转换
        print(0)
        exit()
    StringList=[]
    for _ in range(n):
        StringList.append(input())
    visited=[False for i in range(n)]
    que=[[beginStr,1]]
    while que:
        str,step=que.pop(0)
        if judge(str,endStr):
            print(step+1) #只有一个不一样，直接输出结果
            exit()
        for i in range(n):#和列表里的一个个去匹配
            if visited[i]==False and judge(StringList[i],str):
                visited[i]=True
                que.append([StringList[i],step+1])
    print(0)
        
