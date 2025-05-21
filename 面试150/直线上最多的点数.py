class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n=len(points)
        if n<=2:
            return n
        def get_slope(p1,p2):
            dx=p2[0]-p1[0]
            dy=p2[1]-p1[1]
            if dx==0:
                return ('inf',0)
            if dy==0:
                return (0,'inf')
            d=gcd(dx,dy)
            return (dy//d,dx//d)
        max_points=0
        for i in range(n):
            slopes=defaultdict(int)
            dup=0
            cur_max=0
            for j in range(n):
                if i==j:
                    continue
                if points[i]==points[j]:
                    dup+=1
                else:
                    slope=get_slope(points[i],points[j])
                    slopes[slope]+=1
                    cur_max=max(cur_max,slopes[slope])
            max_points=max(max_points,cur_max+dup+1)
        return max_points
