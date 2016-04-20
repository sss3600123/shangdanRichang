<?php

/* --------------------------------------------------------------------------*/
/**
* @tianxiaolong  
*
* @Param [5
* @Param '5'
* @Param '05'
* @Param 12.3
* @Param '16.7'
* @Param 'five'
* @Param 0xDECAFBAD
* @Param $maybeNumber
* is_numeric() 判断是否是数字
* gettype() 获取变量类型
 */
/* ----------------------------------------------------------------------------*/
foreach ([5, '5', '05', 12.3, '16.7', 'five', 0xDECAFBAD, 10e200, "5,100"] as $maybeNumber) {
	$isItNumber = is_numeric($maybeNumber);
	$actualType = gettype($maybeNumber);
	print "Is the $actualType $maybeNumber numeric? ";
	if (is_numeric($maybeNumber)) {
		print "yes";
	} else {
		print "no";
	}	
	print "<br/>";
}

print "<br/>";

//$number = "5,100";
//$withCommas = is_numeric($number);

