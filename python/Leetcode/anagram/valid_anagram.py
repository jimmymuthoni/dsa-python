class Solution:
  def isAnagram(self, s:str, t:str) -> bool:
    if len(s) != len(t):
        return False

    freq = [0] * 26 
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    for ch in t:
        index = ord(ch) - ord('a')
        freq[index] -= 1
        if freq[index] < 0:
            return False
    return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram(s="cat",t="act"))

#time complexity O(n) ---> processes each character once
#space complexity 0(1) ----> fixed array length 26


