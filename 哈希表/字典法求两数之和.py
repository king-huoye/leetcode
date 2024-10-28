class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}  # 新建一个字典用于存储数值和对应的索引
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in result:  # 如果 target - nums[i] 在字典中，返回结果
                return [result[tmp], i]
            result[nums[i]] = i  # 将当前数值和它的索引存入字典
