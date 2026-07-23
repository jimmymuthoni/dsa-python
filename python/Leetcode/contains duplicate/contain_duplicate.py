from typing import List
class Solution:
    def contains_duplicate(self,nums:List[int])->bool:
        distict_values = set()
        for num in nums:
            if num in distict_values:
                return True
            distict_values.add(num)
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.contains_duplicate([2,7,8,9,12,44,1,5,2]))