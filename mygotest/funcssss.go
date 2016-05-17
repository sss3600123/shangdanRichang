package main

import "fmt"

func plus (a int, b int) int {
	return a + b
}

/* --------------------------------------------------------------------------*/
/**
* @tianxiaolong  
*
* @Param a
* @Param b
* @Param int
* 括号内参数类型，括号外 返回值类型 （函数类型）
* @Returns   
*/
/* ----------------------------------------------------------------------------*/
func plusPlus (a, b, c int) int {
	return a + b + c
}

func main () {
	res := plus(1, 2)
	fmt.Println("1+2=", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}
