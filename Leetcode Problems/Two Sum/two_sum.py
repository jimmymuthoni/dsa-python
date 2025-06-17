from typing import List

class Solution:
    def two_sum(self, nums:List[int], target: int) -> List[int]:
        num_indicies = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_indicies:
                return[num_indicies[difference], i]
            num_indicies[num] = i

if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))

