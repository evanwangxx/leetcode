/*
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.

Input:  [4,3,2,7,8,2,3,1]
Output: [5,6]

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
*/
package main

import "fmt"

func findDisappearedNumbers(nums []int) []int {
	var ret []int
	length := len(nums)
	for i := 0; i < length; i++ {
		if nums[i] != nums[nums[i]-1] {
			nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
			i--
		}
	}
	for i := 0; i < length; i++ {
		if (i + 1) != nums[i] {
			ret = append(ret, (i + 1))
		}
	}
	return ret
}

func sliceEqual(want, ret []int) bool {
	len1 := len(want)
	len2 := len(ret)

	if len1 != len2 {
		return false
	}
	for i := 0; i < len1; i++ {
		if want[i] != ret[i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("phahah")
	input := [] int{4, 3, 2, 7, 8, 2, 3, 1}
	want := [] int{5, 6}

	ret := findDisappearedNumbers(input)

	ok := sliceEqual(want, ret)
	if ok {
		fmt.Println("phahah")
	} else {
		fmt.Println("phahah")
	}
}
