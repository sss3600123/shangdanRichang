<?php

/* --------------------------------------------------------------------------*/
/**
* @tianxiaolong
*
* @Param $length
* @Param $characters
*
* @Returns
* mt_rand() 梅森旋转算法，比rand 快4倍
 */
/* ----------------------------------------------------------------------------*/
/**
 * [str_rand description]
 * @param  integer $length     [description]
 * @param  string  $characters [description]
 * @return [type]              [description]
 */
function str_rand($length = 32, $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
{
	if (!is_int($length) || $length < 0) {
		return false;
	}

	$characters_length = strlen($characters) - 1;
	$string = '';
	for ($i = $length; $i > 0; $i--) {
		$string .= $characters[mt_rand(0, $characters_length)];
	}
	return $string;
}

//$str1 = '你好，我是中国人';
//print $str1[2];
print str_rand(4);
