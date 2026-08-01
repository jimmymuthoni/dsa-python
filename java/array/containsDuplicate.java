import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums){
        //create a hashset to store the elements from the array
        HashSet<Integer> seenNumbers = new HashSet<>();

        //loop through the array 
        for (int num : nums){
            //check if the elements is already in the array
            if (seenNumbers.contains(num)){
                return true; //Duplicate found
            }
            //add the element to the hashset
            seenNumbers.add(num);
        }
        return false; //no duplicate found
    }
}