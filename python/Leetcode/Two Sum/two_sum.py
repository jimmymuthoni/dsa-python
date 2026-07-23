from typing import List
class Solution:
    def two_sum(self,nums:List[int], target:int)->List[int]:
        hash_map = {}
        for i,num in enumerate(nums):
            difference = target - num
            if difference in hash_map:
                return[hash_map[difference],i]
            hash_map[num] = i
if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([2,7,11,15],20))