import java.util.HashSet;

class Solution {
    public boolean containsDuplicateTwo(int[] nums, int k){
        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i ++){
            if (set.contains(nums[i])) return true;
            set.add(nums[i]);
            if (set.size() > k) {
                set.remove(nums[i -k]);
            }
        }
        return false;
}
}