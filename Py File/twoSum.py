from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i

so = Solution()
nums = [3,2,4]
target = 6
nums = [2,7,11,15]
target = 18
print(so.twoSum(nums, target))
