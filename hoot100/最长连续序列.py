class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length=0
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:
                # 检查开头
                cur=num
                cur_lenth=1
                while cur+1 in num_set:
                    cur+=1
                    cur_lenth+=1
                length=max(length,cur_lenth)
        return length
