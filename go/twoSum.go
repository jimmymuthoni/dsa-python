package main

import "fmt"

func twoSum(nums []int, target int) []int {

	hashMap := make(map[int]int)

	for i, num := range nums {

		diff := target - num

		if index, exists := hashMap[diff]; exists {
			return []int{index, i}
		}

		hashMap[num] = i
	}

	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	fmt.Println(twoSum(nums, target))
}