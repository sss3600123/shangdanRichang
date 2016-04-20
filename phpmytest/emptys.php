<?php
	$a = ' ';
	$b = null;
		
	/* --------------------------------------------------------------------------*/
	/**
		* @tianxiaolong  
		*
		* @Param $a 以后用这个方法判断空，空字符串。空格
	 */
	/* ----------------------------------------------------------------------------*/
	if(trim($a) == false)
	{
		echo "a is kk";
	}
	else
	{
		echo "a is not kk";
	}
	echo '<br/>';
	if(empty($b))
	{
		echo "b is kk";
	}
	else
	{
		echo "b is not kk";
	}

	echo '<br/>';
	if(empty($c))
	{
		echo 'c is kk';
	}
	else
	{
		echo 'c is not kk';
	}
