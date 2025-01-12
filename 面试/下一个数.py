class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        if num==2147483647:
            return [-1,-1]
        le = str(bin(num)).count('1') # 计算 num 的二进制表示中 "1" 的个数
        res = [num + 1, num - 1]#从num的下一个数或前一个数去尝试
        while str(bin(res[0])).count('1') != le:
            res[0] += 1
        while str(bin(res[1])).count('1') != le:
            res[1] -= 1
        return res

