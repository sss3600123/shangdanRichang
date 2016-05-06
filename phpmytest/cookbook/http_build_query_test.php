<?php

$vars = [
	'name' => 'Oscar the Grouth',
	'color' => 'green',
	'favorite_punctuation' => '#'	
];

/* --------------------------------------------------------------------------*/
/**
	* @tianxiaolong  
	*
	* @Param $vars
	* http_build_query 将数组转成get方式
	* @Returns   
 */
/* ----------------------------------------------------------------------------*/
$query_string = http_build_query($vars);
$url = '/muppet/select.php?'.$query_string;
echo $url;
