import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        // HashMap to store numbers and their indices.
        Map<Integer, Integer> map = new HashMap<>();

        // Iterate through the array.
        for (int i = 0; i < nums.length; i++) {

            // Difference needed to reach target
            int diff = target - nums[i];

            // Check if difference exists in map
            if (map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }

            // Store current number and its index
            map.put(nums[i], i);
        }

        // No solution found 
        return new int[]{};
    }
}