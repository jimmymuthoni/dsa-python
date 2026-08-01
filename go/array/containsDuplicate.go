package array

func containsDuplicate(nums []int) bool {
	//create a hashset
	distictValues := make(map[int]bool)

	//loop through the array
	for _, num := range nums {
		//check iff the number is already in the set
		if distictValues[num] {
			return true
		}
		//add the number in the set
		distictValues[num] = true
	}
	//no duplicates found
	return false
}