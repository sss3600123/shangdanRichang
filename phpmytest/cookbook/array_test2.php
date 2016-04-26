<?php

$whig_presidents = array(9 => 'Harrison', 'Tyler', 12 => 'Taylor', 'Fillmore');
var_dump($whig_presidents);
echo "<br/>";

$arr1 = ['apple', 'data', 'coconut'];

/* --------------------------------------------------------------------------*/
/**
	* @tianxiaolong  
	*
	* @Param $arr1
	* @Param 5
	* @Param ''
	* array_pad 改变数组的长度，多余用空补
	* @Returns   
 */
/* ----------------------------------------------------------------------------*/
$arr2 = array_pad($arr1, 5, '');

var_dump($arr2);
echo "<br/>";

$arr3 = ['a', 'b', 'c', 'd'];
$str2 = join(',', $arr3);
print $str2;


echo "<br/>";

$favorite_foods = [1 => 'artichokes', 'bread', 'cauliflower', 'deviled eggs'];

$food = 'cauliflower';

$position = array_search($food, $favorite_foods);

if ($position !== false) {
	echo "My #$position favorite food is $food";
} else {
	echo "Blech! I hate $food";
}
