def main():
    n,m=map(int,input().split())
    grid=[]
    for _ in range(n):
        grid.append(list(map(int,input().split())))
    sum_land=0 #陆地单元
    cover=0 #相邻
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                sum_land+=1 
                if i-1>=0 and grid[i-1][j]==1:
                    cover+=1 #统计上边相邻陆地
            #统计左边 
                if j-1>=0 and grid[i][j-1]==1:
                    cover+=1 
    result=sum_land*4-cover*2
    print(result)
if __name__ == '__main__':
    main()
