package main

import "fmt"

func main () {
	nums := []int{2, 3, 4}			//数组
	sum := 0
	for _, num := range nums {			//循环数组
		sum += num
		fmt.Println("nums:", num)
	}

	fmt.Println("sum:", sum)

	for i, num := range nums {
		fmt.Println("index:", i, "num:", num)
	}

	kvs := map[string]string{"a": "apple", "b": "banana"}

	for k, v := range kvs {				//循环map
		fmt.Println("keys:", k, "vals:", v)
	}

	for i, c := range "golang" {
		fmt.Println(i, c)
	}

}
