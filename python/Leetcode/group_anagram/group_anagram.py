from typing import List
class Solution:
    def group_anagram(self, strs:List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        
        ans_map = {}
        for s in strs:
            count = [0] * 26       
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key_part = []

            for num in count:
                key_part.append("#")
                key_part.append(str(num))
            key = "".join(key_part)

            if key not in ans_map:
                ans_map[key] = []
            ans_map[key].append(s)

        return list(ans_map.values())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.group_anagram(['eat','tea','tan','ate','nat','bat']))


"""
Tme complexity; O(N*K)
 - N: number of drings
 -K: average length of each string

Space complexity: O(N*K)
"""
            
        